import typing
import collections.abc
import typing_extensions
import bpy.types
import bpy.typing

def armature_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    selected: bool | None = False,
):
    """Apply the current pose as the new rest pose

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param selected: Selected Only, Only apply the selected bones (with propagation to children)
    :type selected: bool | None
    """

def autoside_names(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    axis: typing.Literal["XAXIS", "YAXIS", "ZAXIS"] | None = "XAXIS",
):
    """Automatically renames the selected bones according to which side of the target axis they fall on

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param axis: Axis, Axis to tag names with

    XAXIS
    X-Axis -- Left/Right.

    YAXIS
    Y-Axis -- Front/Back.

    ZAXIS
    Z-Axis -- Top/Bottom.
        :type axis: typing.Literal['XAXIS','YAXIS','ZAXIS'] | None
    """

def blend_to_neighbor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
):
    """Blend from current position to previous or next keyframe

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: float | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: int | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: int | None
        :param channels: Channels, Set of properties that are affected

    ALL
    All Properties -- All properties, including transforms, bendy bone shape, and custom properties.

    LOC
    Location -- Location only.

    ROT
    Rotation -- Rotation only.

    SIZE
    Scale -- Scale only.

    BBONE
    Bendy Bone -- Bendy Bone shape properties.

    CUSTOM
    Custom Properties -- Custom properties.
        :type channels: typing.Literal['ALL','LOC','ROT','SIZE','BBONE','CUSTOM'] | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: typing.Literal['FREE','X','Y','Z'] | None
    """

def blend_with_rest(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
):
    """Make the current pose more similar to, or further away from, the rest pose

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: float | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: int | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: int | None
        :param channels: Channels, Set of properties that are affected

    ALL
    All Properties -- All properties, including transforms, bendy bone shape, and custom properties.

    LOC
    Location -- Location only.

    ROT
    Rotation -- Rotation only.

    SIZE
    Scale -- Scale only.

    BBONE
    Bendy Bone -- Bendy Bone shape properties.

    CUSTOM
    Custom Properties -- Custom properties.
        :type channels: typing.Literal['ALL','LOC','ROT','SIZE','BBONE','CUSTOM'] | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: typing.Literal['FREE','X','Y','Z'] | None
    """

def breakdown(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
):
    """Create a suitable breakdown pose on the current frame

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: float | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: int | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: int | None
        :param channels: Channels, Set of properties that are affected

    ALL
    All Properties -- All properties, including transforms, bendy bone shape, and custom properties.

    LOC
    Location -- Location only.

    ROT
    Rotation -- Rotation only.

    SIZE
    Scale -- Scale only.

    BBONE
    Bendy Bone -- Bendy Bone shape properties.

    CUSTOM
    Custom Properties -- Custom properties.
        :type channels: typing.Literal['ALL','LOC','ROT','SIZE','BBONE','CUSTOM'] | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: typing.Literal['FREE','X','Y','Z'] | None
    """

def constraint_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: bpy.typing.ConstraintTypeItems | None = "",
):
    """Add a constraint to the active bone

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.typing.ConstraintTypeItems | None
    """

def constraint_add_with_targets(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: bpy.typing.ConstraintTypeItems | None = "",
):
    """Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.typing.ConstraintTypeItems | None
    """

def constraints_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear all constraints from the selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def constraints_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy constraints to other selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the current pose of the selected bones to the internal clipboard

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def flip_names(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    do_strip_numbers: bool | None = False,
):
    """Flips (and corrects) the axis suffixes of the names of selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names.Warning: May result in incoherent naming in some cases
    :type do_strip_numbers: bool | None
    """

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | None = False,
):
    """Tag selected bones to not be visible in Pose Mode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected
    :type unselected: bool | None
    """

def ik_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    with_targets: bool | None = True,
):
    """Add IK Constraint to the active Bone

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects
    :type with_targets: bool | None
    """

def ik_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove all IK Constraints from selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def loc_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset locations of selected bones to their default values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    flipped: bool | None = False,
    selected_mask: bool | None = False,
):
    """Paste the stored pose on to the current pose

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose
    :type flipped: bool | None
    :param selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose
    :type selected_mask: bool | None
    """

def paths_calculate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    display_type: bpy.typing.MotionpathDisplayTypeItems | None = "RANGE",
    range: bpy.typing.MotionpathRangeItems | None = "SCENE",
    bake_location: bpy.typing.MotionpathBakeLocationItems | None = "HEADS",
):
    """Calculate paths for the selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param display_type: Display type
    :type display_type: bpy.typing.MotionpathDisplayTypeItems | None
    :param range: Computation Range
    :type range: bpy.typing.MotionpathRangeItems | None
    :param bake_location: Bake Location, Which point on the bones is used when calculating paths
    :type bake_location: bpy.typing.MotionpathBakeLocationItems | None
    """

def paths_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_selected: bool | None = False,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_selected: Only Selected, Only clear motion paths of selected bones
    :type only_selected: bool | None
    """

def paths_range_update(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Update frame range for motion paths from the Scene's current frame range

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def paths_update(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Recalculate paths for bones that already have them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def propagate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal[
        "NEXT_KEY",
        "LAST_KEY",
        "BEFORE_FRAME",
        "BEFORE_END",
        "SELECTED_KEYS",
        "SELECTED_MARKERS",
    ]
    | None = "NEXT_KEY",
    end_frame: float | None = 250.0,
):
    """Copy selected aspects of the current pose to subsequent poses already keyframed

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Terminate Mode, Method used to determine when to stop propagating pose to keyframes

    NEXT_KEY
    To Next Keyframe -- Propagate pose to first keyframe following the current frame only.

    LAST_KEY
    To Last Keyframe -- Propagate pose to the last keyframe only (i.e. making action cyclic).

    BEFORE_FRAME
    Before Frame -- Propagate pose to all keyframes between current frame and 'Frame' property.

    BEFORE_END
    Before Last Keyframe -- Propagate pose to all keyframes from current frame until no more are found.

    SELECTED_KEYS
    On Selected Keyframes -- Propagate pose to all selected keyframes.

    SELECTED_MARKERS
    On Selected Markers -- Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.
        :type mode: typing.Literal['NEXT_KEY','LAST_KEY','BEFORE_FRAME','BEFORE_END','SELECTED_KEYS','SELECTED_MARKERS'] | None
        :param end_frame: End Frame, Frame to stop propagating frames to (for 'Before Frame' mode)
        :type end_frame: float | None
    """

def push(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
):
    """Exaggerate the current pose in regards to the breakdown pose

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: float | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: int | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: int | None
        :param channels: Channels, Set of properties that are affected

    ALL
    All Properties -- All properties, including transforms, bendy bone shape, and custom properties.

    LOC
    Location -- Location only.

    ROT
    Rotation -- Rotation only.

    SIZE
    Scale -- Scale only.

    BBONE
    Bendy Bone -- Bendy Bone shape properties.

    CUSTOM
    Custom Properties -- Custom properties.
        :type channels: typing.Literal['ALL','LOC','ROT','SIZE','BBONE','CUSTOM'] | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: typing.Literal['FREE','X','Y','Z'] | None
    """

def quaternions_flip(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flip quaternion values to achieve desired rotations, while maintaining the same orientations

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def relax(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
):
    """Make the current pose more similar to its breakdown pose

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: float | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: int | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: int | None
        :param channels: Channels, Set of properties that are affected

    ALL
    All Properties -- All properties, including transforms, bendy bone shape, and custom properties.

    LOC
    Location -- Location only.

    ROT
    Rotation -- Rotation only.

    SIZE
    Scale -- Scale only.

    BBONE
    Bendy Bone -- Bendy Bone shape properties.

    CUSTOM
    Custom Properties -- Custom properties.
        :type channels: typing.Literal['ALL','LOC','ROT','SIZE','BBONE','CUSTOM'] | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: typing.Literal['FREE','X','Y','Z'] | None
    """

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | None = True,
):
    """Reveal all bones hidden in Pose Mode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def rot_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset rotations of selected bones to their default values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rotation_mode_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: bpy.typing.ObjectRotationModeItems | None = "QUATERNION",
):
    """Set the rotation representation used by selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rotation Mode
    :type type: bpy.typing.ObjectRotationModeItems | None
    """

def scale_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset scaling of selected bones to their default values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Toggle selection status of all bones

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

def select_constraint_target(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select bones used as targets for the currently selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_grouped(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | None = False,
    type: typing.Literal["COLLECTION", "COLOR", "KEYINGSET"] | None = "COLLECTION",
):
    """Select all visible bones grouped by similar properties

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param extend: Extend, Extend selection instead of deselecting everything first
        :type extend: bool | None
        :param type: Type

    COLLECTION
    Collection -- Same collections as the active bone.

    COLOR
    Color -- Same color as the active bone.

    KEYINGSET
    Keying Set -- All bones affected by active Keying Set.
        :type type: typing.Literal['COLLECTION','COLOR','KEYINGSET'] | None
    """

def select_hierarchy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: typing.Literal["PARENT", "CHILD"] | None = "PARENT",
    extend: bool | None = False,
):
    """Select immediate parent/children of selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: typing.Literal['PARENT','CHILD'] | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all bones linked by parent/child connections to the current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | None = False,
):
    """Select bones linked by parent/child connections under the mouse cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    """

def select_mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_active: bool | None = False,
    extend: bool | None = False,
):
    """Mirror the bone selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Active Only, Only operate on the active bone
    :type only_active: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_parent(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select bones that are parents of the currently selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a new empty Selection Set

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_add_and_assign(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a new Selection Set with the currently selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_assign(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add selected bones to Selection Set

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the selected Selection Set(s) to the clipboard

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_delete_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove all Selection Sets from this Armature

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_deselect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove Selection Set bones from current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move the active Selection Set up/down the list of sets

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Move Direction, Direction to move the active Selection Set: UP (default) or DOWN
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def selection_set_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add new Selection Set(s) from the clipboard

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove a Selection Set from this Armature

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_remove_bones(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the selected bones from all Selection Sets

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selection_set_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    selection_set_index: int | None = -1,
):
    """Select the bones from this Selection Set

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param selection_set_index: Selection Set Index, Which Selection Set to select; -1 uses the active Selection Set
    :type selection_set_index: int | None
    """

def selection_set_unassign(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove selected bones from Selection Set

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def transforms_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset location, rotation, and scaling of selected bones to their default values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def user_transforms_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_selected: bool | None = True,
):
    """Reset pose bone transforms to keyframed state

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_selected: Only Selected, Only visible/selected bones
    :type only_selected: bool | None
    """

def visual_transform_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply final constrained position of pose bones to their transform

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """
