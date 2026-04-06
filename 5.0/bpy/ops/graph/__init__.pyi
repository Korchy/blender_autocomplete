import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types

def bake_keys(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add keyframes on every frame between the selected keyframes"""

def blend_offset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
) -> None:
    """Shift selected keys to the value of the neighboring keys as a block

    :param factor: Offset Factor, Control which key to offset towards and how far
    """

def blend_to_default(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
) -> None:
    """Blend selected keys to their default value from their current position

    :param factor: Factor, How much to blend to the default value
    """

def blend_to_ease(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
) -> None:
    """Blends keyframes from current state to an ease-in or ease-out curve

    :param factor: Blend, Favor either original data or ease curve
    """

def blend_to_neighbor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
) -> None:
    """Blend selected keyframes to their left or right neighbor

    :param factor: Blend, The blend factor with 0 being the current frame
    """

def breakdown(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
) -> None:
    """Move selected keyframes to an inbetween position relative to adjacent keys

    :param factor: Factor, Favor either the left or the right key
    """

def butterworth_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    cutoff_frequency: float | None = 3.0,
    filter_order: int | None = 4,
    samples_per_frame: int | None = 1,
    blend: float | None = 1.0,
    blend_in_out: int | None = 1,
) -> None:
    """Smooth an F-Curve while maintaining the general shape of the curve

    :param cutoff_frequency: Frequency Cutoff (Hz), Lower values give a smoother curve
    :param filter_order: Filter Order, Higher values produce a harder frequency cutoff
    :param samples_per_frame: Samples per Frame, How many samples to calculate per frame, helps with subframe data
    :param blend: Blend, How much to blend to the smoothed curve
    :param blend_in_out: Blend In/Out, Linearly blend the smooth data to the border frames of the selection
    """

def clean(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.001,
    channels: bool | None = False,
) -> None:
    """Simplify F-Curves by removing closely spaced keyframes

    :param threshold: Threshold
    :param channels: Channels
    """

def click_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: float | None = 1.0,
    value: float | None = 1.0,
    extend: bool | None = False,
) -> None:
    """Insert new keyframe at the cursor position for the active F-Curve

    :param frame: Frame Number, Frame to insert keyframe on
    :param value: Value, Value for keyframe on
    :param extend: Extend, Extend selection instead of deselecting everything first
    """

def clickselect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    use_select_on_click: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    deselect_all: bool | None = False,
    column: bool | None = False,
    curves: bool | None = False,
) -> None:
    """Select keyframes by clicking on them

    :param wait_to_deselect_others: Wait to Deselect Others
    :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if theres drag event. Otherwise select on mouse release
    :param mouse_x: Mouse X
    :param mouse_y: Mouse Y
    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
    :param curves: Only Curves, Select all the keyframes in the curve
    """

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy selected keyframes to the internal clipboard"""

def cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: float | None = 0.0,
    value: float | None = 0.0,
) -> None:
    """Interactively set the current frame and value cursor

    :param frame: Frame
    :param value: Value
    """

def decimate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["RATIO", "ERROR"] | None = "RATIO",
    factor: float | None = 0.333333,
    remove_error_margin: float | None = 0.0,
) -> None:
    """Decimate F-Curves by removing keyframes that influence the curve shape the least

        :param mode: Mode, Which mode to use for decimation

    RATIO
    Ratio -- Use a percentage to specify how many keyframes you want to remove.

    ERROR
    Error Margin -- Use an error margin to specify how much the curve is allowed to deviate from the original path.
        :param factor: Factor, The ratio of keyframes to remove
        :param remove_error_margin: Max Error Margin, How much the new decimated curve is allowed to deviate from the original
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Remove all selected keyframes

    :param confirm: Confirm, Prompt for confirmation
    """

def driver_delete_invalid(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete all visible drivers considered invalid"""

def driver_variables_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the driver variables of the active driver"""

def driver_variables_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    replace: bool | None = False,
) -> None:
    """Add copied driver variables to the active driver

    :param replace: Replace Existing, Replace existing driver variables, instead of just appending to the end of the existing list
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: bpy.stub_internal.rna_enums.TransformModeTypeItems | None = "TRANSLATION",
) -> None:
    """Make a copy of all selected keyframes

    :param mode: Mode
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    GRAPH_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Make a copy of all selected keyframes and move them

    :param GRAPH_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def ease(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
    sharpness: float | None = 2.0,
) -> None:
    """Align keyframes on a ease-in or ease-out curve

    :param factor: Curve Bend, Defines if the keys should be aligned on an ease-in or ease-out curve
    :param sharpness: Sharpness, Higher values make the change more abrupt
    """

def easing_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.BeztripleInterpolationEasingItems | None = "AUTO",
) -> None:
    """Set easing type for the F-Curve segments starting from the selected keyframes

    :param type: Type
    """

def equalize_handles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    side: typing.Literal["LEFT", "RIGHT", "BOTH"] | None = "LEFT",
    handle_length: float | None = 5.0,
    flatten: bool | None = False,
) -> None:
    """Ensure selected keyframes handles have equal length, optionally making them horizontal. Automatic, Automatic Clamped, or Vector handle types will be converted to Aligned

        :param side: Side, Side of the keyframes Bézier handles to affect

    LEFT
    Left -- Equalize selected keyframes left handles.

    RIGHT
    Right -- Equalize selected keyframes right handles.

    BOTH
    Both -- Equalize both of a keyframes handles.
        :param handle_length: Handle Length, Length to make selected keyframes Bézier handles
        :param flatten: Flatten, Make the values of the selected keyframes handles the same as their respective keyframes
    """

def euler_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics"""

def extrapolation_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CONSTANT", "LINEAR", "MAKE_CYCLIC", "CLEAR_CYCLIC"]
    | None = "CONSTANT",
) -> None:
    """Set extrapolation mode for selected F-Curves

        :param type: Type

    CONSTANT
    Constant Extrapolation -- Values on endpoint keyframes are held.

    LINEAR
    Linear Extrapolation -- Straight-line slope of end segments are extended past the endpoint keyframes.

    MAKE_CYCLIC
    Make Cyclic (F-Modifier) -- Add Cycles F-Modifier if one does not exist already.

    CLEAR_CYCLIC
    Clear Cyclic (F-Modifier) -- Remove Cycles F-Modifier if not needed anymore.
    """

def fmodifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.FmodifierTypeItems | None = "NULL",
    only_active: bool | None = False,
) -> None:
    """Add F-Modifier to the active/selected F-Curves

    :param type: Type
    :param only_active: Only Active, Only add F-Modifier to active F-Curve
    """

def fmodifier_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the F-Modifier(s) of the active F-Curve"""

def fmodifier_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_active: bool | None = False,
    replace: bool | None = False,
) -> None:
    """Add copied F-Modifiers to the selected F-Curves

    :param only_active: Only Active, Only paste F-Modifiers on active F-Curve
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
    """

def frame_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Place the cursor on the midpoint of selected keyframes"""

def gaussian_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.0,
    sigma: float | None = 0.33,
    filter_width: int | None = 6,
) -> None:
    """Smooth the curve using a Gaussian filter

    :param factor: Factor, How much to blend to the default value
    :param sigma: Sigma, The shape of the gaussian distribution, lower values make it sharper
    :param filter_width: Filter Width, How far to each side the operator will average the key values
    """

def ghost_curves_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear F-Curve snapshots (Ghosts) for active Graph Editor"""

def ghost_curves_create(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor"""

def handle_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.KeyframeHandleTypeItems | None = "FREE",
) -> None:
    """Set type of handle for selected keyframes

    :param type: Type
    """

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide selected curves from Graph Editor view

    :param unselected: Unselected, Hide unselected rather than selected curves
    """

def interpolation_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.BeztripleInterpolationModeItems
    | None = "CONSTANT",
) -> None:
    """Set interpolation mode for the F-Curve segments starting from the selected keyframes

    :param type: Type
    """

def keyframe_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["ALL", "SEL", "ACTIVE", "CURSOR_ACTIVE", "CURSOR_SEL"]
    | None = "ALL",
) -> None:
    """Insert keyframes for the specified channels

        :param type: Type

    ALL
    All Channels -- Insert a keyframe on all visible and editable F-Curves using each curves current value.

    SEL
    Only Selected Channels -- Insert a keyframe on selected F-Curves using each curves current value.

    ACTIVE
    Only Active F-Curve -- Insert a keyframe on the active F-Curve using the curves current value.

    CURSOR_ACTIVE
    Active Channels at Cursor -- Insert a keyframe for the active F-Curve at the cursor point.

    CURSOR_SEL
    Selected Channels at Cursor -- Insert a keyframe for selected F-Curves at the cursor point.
    """

def keyframe_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    next: bool | None = True,
) -> None:
    """Jump to previous/next keyframe

    :param next: Next Keyframe
    """

def keys_to_samples(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Convert selected channels to an uneditable set of samples to save storage space"""

def match_slope(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
) -> None:
    """Blend selected keys to the slope of neighboring ones

    :param factor: Factor, Defines which keys to use as slope and how much to blend towards them
    """

def mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CFRA", "VALUE", "YAXIS", "XAXIS", "MARKER"] | None = "CFRA",
) -> None:
    """Flip selected keyframes over the selected mirror line

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
    """

def paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: bpy.stub_internal.rna_enums.KeyframePasteOffsetItems | None = "START",
    value_offset: bpy.stub_internal.rna_enums.KeyframePasteOffsetValueItems
    | None = "NONE",
    merge: bpy.stub_internal.rna_enums.KeyframePasteMergeItems | None = "MIX",
    flipped: bool | None = False,
) -> None:
    """Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

    :param offset: Frame Offset, Paste time offset of keys
    :param value_offset: Value Offset, Paste keys with a value offset
    :param merge: Type, Method of merging pasted keys and existing
    :param flipped: Flipped, Paste keyframes from mirrored bones if they exist
    """

def previewrange_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set Preview Range based on range of selected keyframes"""

def push_pull(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.0,
) -> None:
    """Exaggerate or minimize the value of the selected keys

    :param factor: Factor, Control how far to push or pull the keys
    """

def reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Make previously hidden curves visible again in Graph Editor view

    :param select: Select
    """

def samples_to_keys(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Convert selected channels from samples to keyframes"""

def scale_average(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.0,
) -> None:
    """Scale selected key values by their combined average

    :param factor: Scale Factor, The scale factor applied to the curve segments
    """

def scale_from_neighbor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
    anchor: typing.Literal["LEFT", "RIGHT"] | None = "LEFT",
) -> None:
    """Increase or decrease the value of selected keys in relationship to the neighboring one

    :param factor: Factor, The factor to scale keys with
    :param anchor: Reference Key, Which end of the segment to use as a reference to scale from
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Toggle selection of all keyframes

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Select all keyframes within the specified region

        :param axis_range: Axis Range
        :param include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys
        :param tweak: Tweak, Operator has been activated using a click-drag event
        :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the calculated F-curve
        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_circle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    radius: int | None = 25,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    include_handles: bool | None = True,
    use_curve_selection: bool | None = True,
) -> None:
    """Select keyframe points using circle selection

        :param x: X
        :param y: Y
        :param radius: Radius
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :param include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys
        :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
    """

def select_column(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["KEYS", "CFRA", "MARKERS_COLUMN", "MARKERS_BETWEEN"]
    | None = "KEYS",
) -> None:
    """Select all keyframes on the specified frame(s)

    :param mode: Mode
    """

def select_key_handles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    left_handle_action: typing.Literal["SELECT", "DESELECT", "KEEP"] | None = "SELECT",
    right_handle_action: typing.Literal["SELECT", "DESELECT", "KEEP"] | None = "SELECT",
    key_action: typing.Literal["SELECT", "DESELECT", "KEEP"] | None = "KEEP",
) -> None:
    """For selected keyframes, select/deselect any combination of the key itself and its handles

        :param left_handle_action: Left Handle, Effect on the left handle

    SELECT
    Select.

    DESELECT
    Deselect.

    KEEP
    Keep -- Leave as is.
        :param right_handle_action: Right Handle, Effect on the right handle

    SELECT
    Select.

    DESELECT
    Deselect.

    KEEP
    Keep -- Leave as is.
        :param key_action: Key, Effect on the key itself

    SELECT
    Select.

    DESELECT
    Deselect.

    KEEP
    Keep -- Leave as is.
    """

def select_lasso(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    include_handles: bool | None = True,
    use_curve_selection: bool | None = True,
) -> None:
    """Select keyframe points using lasso selection

        :param path: Path
        :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
        :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
        :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :param include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys
        :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
    """

def select_leftright(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["CHECK", "LEFT", "RIGHT"] | None = "CHECK",
    extend: bool | None = False,
) -> None:
    """Select keyframes to the left or the right of the current frame

    :param mode: Mode
    :param extend: Extend Select
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect keyframes on ends of selection islands"""

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select keyframes occurring in the same F-Curves as selected ones"""

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select keyframes beside already selected ones"""

def shear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.0,
    direction: typing.Literal["FROM_LEFT", "FROM_RIGHT"] | None = "FROM_LEFT",
) -> None:
    """Affect the value of the keys linearly, keeping the same relationship between them using either the left or the right key as reference

        :param factor: Shear Factor, The amount of shear to apply
        :param direction: Direction, Which end of the segment to use as a reference to shear from

    FROM_LEFT
    From Left -- Shear the keys using the left key as reference.

    FROM_RIGHT
    From Right -- Shear the keys using the right key as reference.
    """

def smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Apply weighted moving means to make selected F-Curves less bumpy"""

def snap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Snap selected keyframes to the chosen times/values

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
    """

def snap_cursor_value(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Place the cursor value on the average value of selected keyframes"""

def sound_to_samples(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Bakes a sound wave to samples on selected channels

        :param filepath: File Path, Path to file
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :param filter_blender: Filter .blend files
        :param filter_backup: Filter .blend files
        :param filter_image: Filter image files
        :param filter_movie: Filter movie files
        :param filter_python: Filter Python files
        :param filter_font: Filter font files
        :param filter_sound: Filter sound files
        :param filter_text: Filter text files
        :param filter_archive: Filter archive files
        :param filter_btx: Filter btx files
        :param filter_alembic: Filter Alembic files
        :param filter_usd: Filter USD files
        :param filter_obj: Filter OBJ files
        :param filter_volume: Filter OpenVDB volume files
        :param filter_folder: Filter folders
        :param filter_blenlib: Filter Blender IDs
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :param show_multiview: Enable Multi-View
        :param use_multiview: Use Multi-View
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :param sort_method: File sorting mode
        :param low: Lowest Frequency, Cutoff frequency of a high-pass filter that is applied to the audio data
        :param high: Highest Frequency, Cutoff frequency of a low-pass filter that is applied to the audio data
        :param attack: Attack Time, Value for the envelope calculation that tells how fast the envelope can rise (the lower the value the steeper it can rise)
        :param release: Release Time, Value for the envelope calculation that tells how fast the envelope can fall (the lower the value the steeper it can fall)
        :param threshold: Threshold, Minimum amplitude value needed to influence the envelope
        :param use_accumulate: Accumulate, Only the positive differences of the envelope amplitudes are summarized to produce the output
        :param use_additive: Additive, The amplitudes of the envelope are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated)
        :param use_square: Square, The output is a square curve (negative values always result in -1, and positive ones in 1)
        :param sthreshold: Square Threshold, Square only: all values with an absolute amplitude lower than that result in 0
    """

def time_offset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_offset: float | None = 0.0,
) -> None:
    """Shifts the value of selected keys in time

    :param frame_offset: Frame Offset, How far in frames to offset the animation
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    include_handles: bool | None = True,
) -> None:
    """Reset viewable area to show full keyframe range

    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    """

def view_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move the view to the current frame"""

def view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    include_handles: bool | None = True,
) -> None:
    """Reset viewable area to show selected keyframe range

    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    """
