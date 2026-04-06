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
    channel: bool | None = False,
) -> None:
    """Select keyframes by clicking on them

    :param wait_to_deselect_others: Wait to Deselect Others
    :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if theres drag event. Otherwise select on mouse release
    :param mouse_x: Mouse X
    :param mouse_y: Mouse Y
    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
    :param channel: Only Channel, Select all the keyframes in the channel under the mouse
    """

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy selected keyframes to the internal clipboard"""

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

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make a copy of all selected keyframes"""

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ACTION_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_transform: bpy.ops.transform.transform | None = None,
) -> None:
    """Make a copy of all selected keyframes and move them

    :param ACTION_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
    :param TRANSFORM_OT_transform: Transform, Transform selected items by mode type
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

def frame_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the current frame to the average frame value of selected keyframes"""

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
    type: typing.Literal["ALL", "SEL", "GROUP"] | None = "ALL",
) -> None:
    """Insert keyframes for the specified channels

    :param type: Type
    """

def keyframe_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.BeztripleKeyframeTypeItems | None = "KEYFRAME",
) -> None:
    """Set type of keyframe for the selected keyframes

    :param type: Type
    """

def markers_make_local(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move selected scene markers to the active Action as local pose markers"""

def mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CFRA", "XAXIS", "MARKER"] | None = "CFRA",
) -> None:
    """Flip selected keyframes over the selected mirror line

        :param type: Type

    CFRA
    By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line.

    XAXIS
    By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa).

    MARKER
    By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
    """

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create new action"""

def paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: bpy.stub_internal.rna_enums.KeyframePasteOffsetItems | None = "START",
    merge: bpy.stub_internal.rna_enums.KeyframePasteMergeItems | None = "MIX",
    flipped: bool | None = False,
) -> None:
    """Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

    :param offset: Offset, Paste time offset of keys
    :param merge: Type, Method of merging pasted keys and existing
    :param flipped: Flipped, Paste keyframes from mirrored bones if they exist
    """

def previewrange_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set Preview Range based on extents of selected Keyframes"""

def push_down(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Push action down on to the NLA stack as a new strip"""

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
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    tweak: bool | None = False,
) -> None:
    """Select all keyframes within the specified region

        :param axis_range: Axis Range
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
        :param tweak: Tweak, Operator has been activated using a click-drag event
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

def snap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CFRA", "NEAREST_FRAME", "NEAREST_SECOND", "NEAREST_MARKER"]
    | None = "CFRA",
) -> None:
    """Snap selected keyframes to the times specified

        :param type: Type

    CFRA
    Selection to Current Frame -- Snap selected keyframes to the current frame.

    NEAREST_FRAME
    Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).

    NEAREST_SECOND
    Selection to Nearest Second -- Snap selected keyframes to the nearest second.

    NEAREST_MARKER
    Selection to Nearest Marker -- Snap selected keyframes to the nearest marker.
    """

def stash(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    create_new: bool | None = True,
) -> None:
    """Store this action in the NLA stack as a non-contributing strip for later use

    :param create_new: Create New Action, Create a new action once the existing one has been safely stored
    """

def stash_and_create(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Store this action in the NLA stack as a non-contributing strip for later use, and create a new action"""

def unlink(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    force_delete: bool | None = False,
) -> None:
    """Unlink this action from the active action slot (and/or exit Tweak Mode)

    :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-blocks NLA stack
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset viewable area to show full keyframe range"""

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
) -> None:
    """Reset viewable area to show selected keyframes range"""
