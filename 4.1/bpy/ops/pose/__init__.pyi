import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def armature_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    selected: bool | typing.Any | None = False,
):
    """Apply the current pose as the new rest pose

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param selected: Selected Only, Only apply the selected bones (with propagation to children)
    :type selected: bool | typing.Any | None
    """

    ...

def autoside_names(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    axis: str | None = "XAXIS",
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
        :type axis: str | None
    """

    ...

def blend_to_neighbor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.5,
    prev_frame: typing.Any | None = 0,
    next_frame: typing.Any | None = 0,
    channels: str | None = "ALL",
    axis_lock: str | None = "FREE",
):
    """Blend from current position to previous or next keyframe

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: typing.Any | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: typing.Any | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: typing.Any | None
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
        :type channels: str | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: str | None
    """

    ...

def blend_with_rest(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.5,
    prev_frame: typing.Any | None = 0,
    next_frame: typing.Any | None = 0,
    channels: str | None = "ALL",
    axis_lock: str | None = "FREE",
):
    """Make the current pose more similar to, or further away from, the rest pose

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: typing.Any | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: typing.Any | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: typing.Any | None
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
        :type channels: str | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: str | None
    """

    ...

def breakdown(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.5,
    prev_frame: typing.Any | None = 0,
    next_frame: typing.Any | None = 0,
    channels: str | None = "ALL",
    axis_lock: str | None = "FREE",
):
    """Create a suitable breakdown pose on the current frame

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: typing.Any | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: typing.Any | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: typing.Any | None
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
        :type channels: str | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: str | None
    """

    ...

def constraint_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
):
    """Add a constraint to the active bone

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def constraint_add_with_targets(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
):
    """Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

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

    ...

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

    ...

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

    ...

def flip_names(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    do_strip_numbers: bool | typing.Any | None = False,
):
    """Flips (and corrects) the axis suffixes of the names of selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names.Warning: May result in incoherent naming in some cases
    :type do_strip_numbers: bool | typing.Any | None
    """

    ...

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Tag selected bones to not be visible in Pose Mode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected
    :type unselected: bool | typing.Any | None
    """

    ...

def ik_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    with_targets: bool | typing.Any | None = True,
):
    """Add IK Constraint to the active Bone

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects
    :type with_targets: bool | typing.Any | None
    """

    ...

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

    ...

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

    ...

def paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    flipped: bool | typing.Any | None = False,
    selected_mask: bool | typing.Any | None = False,
):
    """Paste the stored pose on to the current pose

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose
    :type flipped: bool | typing.Any | None
    :param selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose
    :type selected_mask: bool | typing.Any | None
    """

    ...

def paths_calculate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    display_type: str | None = "RANGE",
    range: str | None = "SCENE",
    bake_location: str | None = "HEADS",
):
    """Calculate paths for the selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param display_type: Display type
    :type display_type: str | None
    :param range: Computation Range
    :type range: str | None
    :param bake_location: Bake Location, Which point on the bones is used when calculating paths
    :type bake_location: str | None
    """

    ...

def paths_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_selected: bool | typing.Any | None = False,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_selected: Only Selected, Only clear motion paths of selected bones
    :type only_selected: bool | typing.Any | None
    """

    ...

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

    ...

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

    ...

def propagate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "NEXT_KEY",
    end_frame: typing.Any | None = 250.0,
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
        :type mode: str | None
        :param end_frame: End Frame, Frame to stop propagating frames to (for 'Before Frame' mode)
        :type end_frame: typing.Any | None
    """

    ...

def push(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.5,
    prev_frame: typing.Any | None = 0,
    next_frame: typing.Any | None = 0,
    channels: str | None = "ALL",
    axis_lock: str | None = "FREE",
):
    """Exaggerate the current pose in regards to the breakdown pose

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: typing.Any | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: typing.Any | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: typing.Any | None
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
        :type channels: str | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: str | None
    """

    ...

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

    ...

def relax(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: typing.Any | None = 0.5,
    prev_frame: typing.Any | None = 0,
    next_frame: typing.Any | None = 0,
    channels: str | None = "ALL",
    axis_lock: str | None = "FREE",
):
    """Make the current pose more similar to its breakdown pose

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor, Weighting factor for which keyframe is favored more
        :type factor: typing.Any | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: typing.Any | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: typing.Any | None
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
        :type channels: str | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
        :type axis_lock: str | None
    """

    ...

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
):
    """Reveal all bones hidden in Pose Mode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | typing.Any | None
    """

    ...

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

    ...

def rotation_mode_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "QUATERNION",
):
    """Set the rotation representation used by selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Rotation Mode
    :type type: str | None
    """

    ...

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

    ...

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
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
        :type action: str | None
    """

    ...

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

    ...

def select_grouped(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    type: str | None = "COLLECTION",
):
    """Select all visible bones grouped by similar properties

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param extend: Extend, Extend selection instead of deselecting everything first
        :type extend: bool | typing.Any | None
        :param type: Type

    COLLECTION
    Collection -- Same collections as the active bone.

    COLOR
    Color -- Same color as the active bone.

    KEYINGSET
    Keying Set -- All bones affected by active Keying Set.
        :type type: str | None
    """

    ...

def select_hierarchy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "PARENT",
    extend: bool | typing.Any | None = False,
):
    """Select immediate parent/children of selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: str | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    """

    ...

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

    ...

def select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
):
    """Select bones linked by parent/child connections under the mouse cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | typing.Any | None
    """

    ...

def select_mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_active: bool | typing.Any | None = False,
    extend: bool | typing.Any | None = False,
):
    """Mirror the bone selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Active Only, Only operate on the active bone
    :type only_active: bool | typing.Any | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    """

    ...

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

    ...

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

    ...

def user_transforms_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_selected: bool | typing.Any | None = True,
):
    """Reset pose bone transforms to keyframed state

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_selected: Only Selected, Only visible/selected bones
    :type only_selected: bool | typing.Any | None
    """

    ...

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

    ...
