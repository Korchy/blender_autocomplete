import typing
import collections.abc
import bpy.ops.transform
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

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

    ...

def blend_offset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
):
    """Shift selected keys to the value of the neighboring keys as a block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Offset Factor, Control which key to offset towards and how far
    :type factor: typing.Any | None
    """

    ...

def blend_to_default(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
):
    """Blend selected keys to their default value from their current position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, How much to blend to the default value
    :type factor: typing.Any | None
    """

    ...

def blend_to_ease(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
):
    """Blends keyframes from current state to an ease-in or ease-out curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Blend, Favor either original data or ease curve
    :type factor: typing.Any | None
    """

    ...

def blend_to_neighbor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
):
    """Blend selected keyframes to their left or right neighbor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Blend, The blend factor with 0 being the current frame
    :type factor: typing.Any | None
    """

    ...

def breakdown(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
):
    """Move selected keyframes to an inbetween position relative to adjacent keys

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Favor either the left or the right key
    :type factor: typing.Any | None
    """

    ...

def butterworth_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    cutoff_frequency: typing.Any | None = 3.0,
    filter_order: typing.Any | None = 4,
    samples_per_frame: typing.Any | None = 1,
    blend: typing.Any | None = 1.0,
    blend_in_out: typing.Any | None = 1,
):
    """Smooth an F-Curve while maintaining the general shape of the curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param cutoff_frequency: Frequency Cutoff (Hz), Lower values give a smoother curve
    :type cutoff_frequency: typing.Any | None
    :param filter_order: Filter Order, Higher values produce a harder frequency cutoff
    :type filter_order: typing.Any | None
    :param samples_per_frame: Samples per Frame, How many samples to calculate per frame, helps with subframe data
    :type samples_per_frame: typing.Any | None
    :param blend: Blend, How much to blend to the smoothed curve
    :type blend: typing.Any | None
    :param blend_in_out: Blend In/Out, Linearly blend the smooth data to the border frames of the selection
    :type blend_in_out: typing.Any | None
    """

    ...

def clean(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    threshold: typing.Any | None = 0.001,
    channels: bool | typing.Any | None = False,
):
    """Simplify F-Curves by removing closely spaced keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Threshold
    :type threshold: typing.Any | None
    :param channels: Channels
    :type channels: bool | typing.Any | None
    """

    ...

def click_insert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame: typing.Any | None = 1.0,
    value: typing.Any | None = 1.0,
    extend: bool | typing.Any | None = False,
):
    """Insert new keyframe at the cursor position for the active F-Curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame Number, Frame to insert keyframe on
    :type frame: typing.Any | None
    :param value: Value, Value for keyframe on
    :type value: typing.Any | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | typing.Any | None
    """

    ...

def clickselect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    wait_to_deselect_others: bool | typing.Any | None = False,
    mouse_x: typing.Any | None = 0,
    mouse_y: typing.Any | None = 0,
    extend: bool | typing.Any | None = False,
    deselect_all: bool | typing.Any | None = False,
    column: bool | typing.Any | None = False,
    curves: bool | typing.Any | None = False,
):
    """Select keyframes by clicking on them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: bool | typing.Any | None
    :param mouse_x: Mouse X
    :type mouse_x: typing.Any | None
    :param mouse_y: Mouse Y
    :type mouse_y: typing.Any | None
    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
    :type extend: bool | typing.Any | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | typing.Any | None
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
    :type column: bool | typing.Any | None
    :param curves: Only Curves, Select all the keyframes in the curve
    :type curves: bool | typing.Any | None
    """

    ...

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

    ...

def cursor_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame: typing.Any | None = 0.0,
    value: typing.Any | None = 0.0,
):
    """Interactively set the current frame and value cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame
    :type frame: typing.Any | None
    :param value: Value
    :type value: typing.Any | None
    """

    ...

def decimate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "RATIO",
    factor: typing.Any | None = 0.333333,
    remove_error_margin: typing.Any | None = 0.0,
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
        :type mode: str | None
        :param factor: Remove, The ratio of remaining keyframes after the operation
        :type factor: typing.Any | None
        :param remove_error_margin: Max Error Margin, How much the new decimated curve is allowed to deviate from the original
        :type remove_error_margin: typing.Any | None
    """

    ...

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    confirm: bool | typing.Any | None = True,
):
    """Remove all selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | typing.Any | None
    """

    ...

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

    ...

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

    ...

def driver_variables_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    replace: bool | typing.Any | None = False,
):
    """Add copied driver variables to the active driver

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param replace: Replace Existing, Replace existing driver variables, instead of just appending to the end of the existing list
    :type replace: bool | typing.Any | None
    """

    ...

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "TRANSLATION",
):
    """Make a copy of all selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    """

    ...

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

    ...

def ease(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
):
    """Align keyframes on a ease-in or ease-out curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Curve Bend, Control the bend of the curve
    :type factor: typing.Any | None
    """

    ...

def easing_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "AUTO",
):
    """Set easing type for the F-Curve segments starting from the selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def equalize_handles(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    side: str | None = "LEFT",
    handle_length: typing.Any | None = 5.0,
    flatten: bool | typing.Any | None = False,
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
        :type side: str | None
        :param handle_length: Handle Length, Length to make selected keyframes' Bézier handles
        :type handle_length: typing.Any | None
        :param flatten: Flatten, Make the values of the selected keyframes' handles the same as their respective keyframes
        :type flatten: bool | typing.Any | None
    """

    ...

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

    ...

def extrapolation_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "CONSTANT",
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
        :type type: str | None
    """

    ...

def fmodifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "NULL",
    only_active: bool | typing.Any | None = False,
):
    """Add F-Modifier to the active/selected F-Curves

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param only_active: Only Active, Only add F-Modifier to active F-Curve
    :type only_active: bool | typing.Any | None
    """

    ...

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

    ...

def fmodifier_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_active: bool | typing.Any | None = False,
    replace: bool | typing.Any | None = False,
):
    """Add copied F-Modifiers to the selected F-Curves

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Only Active, Only paste F-Modifiers on active F-Curve
    :type only_active: bool | typing.Any | None
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
    :type replace: bool | typing.Any | None
    """

    ...

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

    ...

def gaussian_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 1.0,
    sigma: typing.Any | None = 0.33,
    filter_width: typing.Any | None = 6,
):
    """Smooth the curve using a Gaussian filter

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, How much to blend to the default value
    :type factor: typing.Any | None
    :param sigma: Sigma, The shape of the gaussian distribution, lower values make it sharper
    :type sigma: typing.Any | None
    :param filter_width: Filter Width, How far to each side the operator will average the key values
    :type filter_width: typing.Any | None
    """

    ...

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

    ...

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

    ...

def handle_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "FREE",
):
    """Set type of handle for selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Hide selected curves from Graph Editor view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected curves
    :type unselected: bool | typing.Any | None
    """

    ...

def interpolation_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "CONSTANT",
):
    """Set interpolation mode for the F-Curve segments starting from the selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def keyframe_insert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "ALL",
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
        :type type: str | None
    """

    ...

def keyframe_jump(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    next: bool | typing.Any | None = True,
):
    """Jump to previous/next keyframe

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param next: Next Keyframe
    :type next: bool | typing.Any | None
    """

    ...

def keys_to_samples(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    confirm: bool | typing.Any | None = True,
):
    """Convert selected channels to an uneditable set of samples to save storage space

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | typing.Any | None
    """

    ...

def match_slope(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
):
    """Blend selected keys to the slope of neighboring ones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Defines which keys to use as slope and how much to blend towards them
    :type factor: typing.Any | None
    """

    ...

def mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "CFRA",
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
        :type type: str | None
    """

    ...

def paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    offset: str | None = "START",
    value_offset: str | None = "NONE",
    merge: str | None = "MIX",
    flipped: bool | typing.Any | None = False,
):
    """Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Frame Offset, Paste time offset of keys
    :type offset: str | None
    :param value_offset: Value Offset, Paste keys with a value offset
    :type value_offset: str | None
    :param merge: Type, Method of merging pasted keys and existing
    :type merge: str | None
    :param flipped: Flipped, Paste keyframes from mirrored bones if they exist
    :type flipped: bool | typing.Any | None
    """

    ...

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

    ...

def push_pull(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 1.0,
):
    """Exaggerate or minimize the value of the selected keys

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Control how far to push or pull the keys
    :type factor: typing.Any | None
    """

    ...

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
):
    """Make previously hidden curves visible again in Graph Editor view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | typing.Any | None
    """

    ...

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

    ...

def scale_average(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 1.0,
):
    """Scale selected key values by their combined average

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Scale Factor, The scale factor applied to the curve segments
    :type factor: typing.Any | None
    """

    ...

def scale_from_neighbor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
    anchor: str | None = "LEFT",
):
    """Increase or decrease the value of selected keys in relationship to the neighboring one

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, The factor to scale keys with
    :type factor: typing.Any | None
    :param anchor: Reference Key, Which end of the segment to use as a reference to scale from
    :type anchor: str | None
    """

    ...

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
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
        :type action: str | None
    """

    ...

def select_box(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    axis_range: bool | typing.Any | None = False,
    include_handles: bool | typing.Any | None = True,
    tweak: bool | typing.Any | None = False,
    use_curve_selection: bool | typing.Any | None = True,
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
    wait_for_input: bool | typing.Any | None = True,
    mode: str | None = "SET",
):
    """Select all keyframes within the specified region

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param axis_range: Axis Range
        :type axis_range: bool | typing.Any | None
        :param include_handles: Include Handles, Are handles tested individually against the selection criteria
        :type include_handles: bool | typing.Any | None
        :param tweak: Tweak, Operator has been activated using a click-drag event
        :type tweak: bool | typing.Any | None
        :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the calculated F-curve
        :type use_curve_selection: bool | typing.Any | None
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
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: str | None
    """

    ...

def select_circle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    x: typing.Any | None = 0,
    y: typing.Any | None = 0,
    radius: typing.Any | None = 25,
    wait_for_input: bool | typing.Any | None = True,
    mode: str | None = "SET",
    use_curve_selection: bool | typing.Any | None = True,
):
    """Select keyframe points using circle selection

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param x: X
        :type x: typing.Any | None
        :param y: Y
        :type y: typing.Any | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | typing.Any | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: str | None
        :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
        :type use_curve_selection: bool | typing.Any | None
    """

    ...

def select_column(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "KEYS",
):
    """Select all keyframes on the specified frame(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    """

    ...

def select_key_handles(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    left_handle_action: str | None = "SELECT",
    right_handle_action: str | None = "SELECT",
    key_action: str | None = "KEEP",
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
        :type left_handle_action: str | None
        :param right_handle_action: Right Handle, Effect on the right handle

    SELECT
    Select.

    DESELECT
    Deselect.

    KEEP
    Keep -- Leave as is.
        :type right_handle_action: str | None
        :param key_action: Key, Effect on the key itself

    SELECT
    Select.

    DESELECT
    Deselect.

    KEEP
    Keep -- Leave as is.
        :type key_action: str | None
    """

    ...

def select_lasso(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    mode: str | None = "SET",
    use_curve_selection: bool | typing.Any | None = True,
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
        :type mode: str | None
        :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
        :type use_curve_selection: bool | typing.Any | None
    """

    ...

def select_leftright(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "CHECK",
    extend: bool | typing.Any | None = False,
):
    """Select keyframes to the left or the right of the current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: str | None
    :param extend: Extend Select
    :type extend: bool | typing.Any | None
    """

    ...

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

    ...

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

    ...

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

    ...

def shear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.0,
    direction: str | None = "FROM_LEFT",
):
    """Affect the value of the keys linearly, keeping the same relationship between them using either the left or the right key as reference

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Shear Factor, The amount of shear to apply
        :type factor: typing.Any | None
        :param direction: Direction, Which end of the segment to use as a reference to shear from

    FROM_LEFT
    From Left -- Shear the keys using the left key as reference.

    FROM_RIGHT
    From Right -- Shear the keys using the right key as reference.
        :type direction: str | None
    """

    ...

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

    ...

def snap(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "CFRA",
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
        :type type: str | None
    """

    ...

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

    ...

def sound_to_samples(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = False,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = True,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = True,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_obj: bool | typing.Any | None = False,
    filter_volume: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 9,
    show_multiview: bool | typing.Any | None = False,
    use_multiview: bool | typing.Any | None = False,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "",
    low: typing.Any | None = 0.0,
    high: typing.Any | None = 100000.0,
    attack: typing.Any | None = 0.005,
    release: typing.Any | None = 0.2,
    threshold: typing.Any | None = 0.0,
    use_accumulate: bool | typing.Any | None = False,
    use_additive: bool | typing.Any | None = False,
    use_square: bool | typing.Any | None = False,
    sthreshold: typing.Any | None = 0.1,
):
    """Bakes a sound wave to samples on selected channels

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter Python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | typing.Any | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | typing.Any | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param low: Lowest Frequency, Cutoff frequency of a high-pass filter that is applied to the audio data
        :type low: typing.Any | None
        :param high: Highest Frequency, Cutoff frequency of a low-pass filter that is applied to the audio data
        :type high: typing.Any | None
        :param attack: Attack Time, Value for the envelope calculation that tells how fast the envelope can rise (the lower the value the steeper it can rise)
        :type attack: typing.Any | None
        :param release: Release Time, Value for the envelope calculation that tells how fast the envelope can fall (the lower the value the steeper it can fall)
        :type release: typing.Any | None
        :param threshold: Threshold, Minimum amplitude value needed to influence the envelope
        :type threshold: typing.Any | None
        :param use_accumulate: Accumulate, Only the positive differences of the envelope amplitudes are summarized to produce the output
        :type use_accumulate: bool | typing.Any | None
        :param use_additive: Additive, The amplitudes of the envelope are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated)
        :type use_additive: bool | typing.Any | None
        :param use_square: Square, The output is a square curve (negative values always result in -1, and positive ones in 1)
        :type use_square: bool | typing.Any | None
        :param sthreshold: Square Threshold, Square only: all values with an absolute amplitude lower than that result in 0
        :type sthreshold: typing.Any | None
    """

    ...

def time_offset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame_offset: typing.Any | None = 0.0,
):
    """Shifts the value of selected keys in time

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame_offset: Frame Offset, How far in frames to offset the animation
    :type frame_offset: typing.Any | None
    """

    ...

def view_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    include_handles: bool | typing.Any | None = True,
):
    """Reset viewable area to show full keyframe range

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool | typing.Any | None
    """

    ...

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

    ...

def view_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    include_handles: bool | typing.Any | None = True,
):
    """Reset viewable area to show selected keyframe range

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool | typing.Any | None
    """

    ...
