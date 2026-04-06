import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def armature_apply(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    selected: bool | None = False,
) -> None:
    """Apply the current pose as the new rest pose

    :param selected: Selected Only, Only apply the selected bones (with propagation to children)
    """

def autoside_names(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: typing.Literal["XAXIS", "YAXIS", "ZAXIS"] | None = "XAXIS",
) -> None:
    """Automatically renames the selected bones according to which side of the target axis they fall on

        :param axis: Axis, Axis to tag names with

    XAXIS
    X-Axis -- Left/Right.

    YAXIS
    Y-Axis -- Front/Back.

    ZAXIS
    Z-Axis -- Top/Bottom.
    """

def blend_to_neighbor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
) -> None:
    """Blend from current position to previous or next keyframe

        :param factor: Factor, Weighting factor for which keyframe is favored more
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
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
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
    """

def blend_with_rest(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
) -> None:
    """Make the current pose more similar to, or further away from, the rest pose

        :param factor: Factor, Weighting factor for which keyframe is favored more
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
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
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
    """

def breakdown(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
) -> None:
    """Create a suitable breakdown pose on the current frame

        :param factor: Factor, Weighting factor for which keyframe is favored more
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
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
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
    """

def constraint_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.ConstraintTypeItems | None = "",
) -> None:
    """Add a constraint to the active bone

    :param type: Type
    """

def constraint_add_with_targets(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.ConstraintTypeItems | None = "",
) -> None:
    """Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

    :param type: Type
    """

def constraints_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear all constraints from the selected bones"""

def constraints_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy constraints to other selected bones"""

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the current pose of the selected bones to the internal clipboard"""

def flip_names(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    do_strip_numbers: bool | None = False,
) -> None:
    """Flips (and corrects) the axis suffixes of the names of selected bones

    :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names.Warning: May result in incoherent naming in some cases
    """

def hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Tag selected bones to not be visible in Pose Mode

    :param unselected: Unselected
    """

def ik_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    with_targets: bool | None = True,
) -> None:
    """Add an IK Constraint to the active Bone. The target can be a selected bone or object

    :param with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects
    """

def ik_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove all IK Constraints from selected bones"""

def loc_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset locations of selected bones to their default values"""

def paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    flipped: bool | None = False,
    selected_mask: bool | None = False,
) -> None:
    """Paste the stored pose on to the current pose

    :param flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose
    :param selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose
    """

def paths_calculate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    display_type: bpy.stub_internal.rna_enums.MotionpathDisplayTypeItems
    | None = "RANGE",
    range: bpy.stub_internal.rna_enums.MotionpathRangeItems | None = "SCENE",
    bake_location: bpy.stub_internal.rna_enums.MotionpathBakeLocationItems
    | None = "HEADS",
) -> None:
    """Calculate paths for the selected bones

    :param display_type: Display Type
    :param range: Computation Range
    :param bake_location: Bake Location, Which point on the bones is used when calculating paths
    """

def paths_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_selected: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

    :param only_selected: Only Selected, Only clear motion paths of selected bones
    """

def paths_range_update(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Update frame range for motion paths from the Scenes current frame range"""

def paths_update(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Recalculate paths for bones that already have them"""

def propagate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
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
) -> None:
    """Copy selected aspects of the current pose to subsequent poses already keyframed

        :param mode: Terminate Mode, Method used to determine when to stop propagating pose to keyframes

    NEXT_KEY
    To Next Keyframe -- Propagate pose to first keyframe following the current frame only.

    LAST_KEY
    To Last Keyframe -- Propagate pose to the last keyframe only (i.e. making action cyclic).

    BEFORE_FRAME
    Before Frame -- Propagate pose to all keyframes between current frame and Frame property.

    BEFORE_END
    Before Last Keyframe -- Propagate pose to all keyframes from current frame until no more are found.

    SELECTED_KEYS
    On Selected Keyframes -- Propagate pose to all selected keyframes.

    SELECTED_MARKERS
    On Selected Markers -- Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.
        :param end_frame: End Frame, Frame to stop propagating frames to (for Before Frame mode)
    """

def push(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
) -> None:
    """Exaggerate the current pose in regards to the breakdown pose

        :param factor: Factor, Weighting factor for which keyframe is favored more
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
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
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
    """

def quaternions_flip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Flip quaternion values to achieve desired rotations, while maintaining the same orientations"""

def relax(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
) -> None:
    """Make the current pose more similar to its breakdown pose

        :param factor: Factor, Weighting factor for which keyframe is favored more
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
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
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE
    Free -- All axes are affected.

    X
    X -- Only X-axis transforms are affected.

    Y
    Y -- Only Y-axis transforms are affected.

    Z
    Z -- Only Z-axis transforms are affected.
    """

def reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Reveal all bones hidden in Pose Mode

    :param select: Select
    """

def rot_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset rotations of selected bones to their default values"""

def rotation_mode_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.ObjectRotationModeItems | None = "QUATERNION",
) -> None:
    """Set the rotation representation used by selected bones

    :param type: Rotation Mode
    """

def scale_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset scaling of selected bones to their default values"""

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Toggle selection status of all bones

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

def select_constraint_target(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select bones used as targets for the currently selected bones"""

def select_grouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    type: typing.Literal[
        "COLLECTION",
        "COLOR",
        "KEYINGSET",
        "CHILDREN",
        "CHILDREN_IMMEDIATE",
        "PARENT",
        "SIBLINGS",
    ]
    | None = "COLLECTION",
) -> None:
    """Select all visible bones grouped by similar properties

        :param extend: Extend, Extend selection instead of deselecting everything first
        :param type: Type

    COLLECTION
    Collection -- Same collections as the active bone.

    COLOR
    Color -- Same color as the active bone.

    KEYINGSET
    Keying Set -- All bones affected by active Keying Set.

    CHILDREN
    Children -- Select all children of currently selected bones.

    CHILDREN_IMMEDIATE
    Immediate Children -- Select direct children of currently selected bones.

    PARENT
    Parents -- Select the parents of currently selected bones.

    SIBLINGS
    Siblings -- Select all bones that have the same parent as currently selected bones.
    """

def select_hierarchy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["PARENT", "CHILD"] | None = "PARENT",
    extend: bool | None = False,
) -> None:
    """Select immediate parent/children of selected bones

    :param direction: Direction
    :param extend: Extend, Extend the selection
    """

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all bones linked by parent/child connections to the current selection"""

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select bones linked by parent/child connections under the mouse cursor

    :param extend: Extend, Extend selection instead of deselecting everything first
    """

def select_mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_active: bool | None = False,
    extend: bool | None = False,
) -> None:
    """Mirror the bone selection

    :param only_active: Active Only, Only operate on the active bone
    :param extend: Extend, Extend the selection
    """

def select_parent(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select bones that are parents of the currently selected bones"""

def selection_set_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new empty Selection Set"""

def selection_set_add_and_assign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new Selection Set with the currently selected bones"""

def selection_set_assign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add selected bones to Selection Set"""

def selection_set_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the selected Selection Set(s) to the clipboard"""

def selection_set_delete_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove all Selection Sets from this Armature"""

def selection_set_deselect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove Selection Set bones from current selection"""

def selection_set_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move the active Selection Set up/down the list of sets

    :param direction: Move Direction, Direction to move the active Selection Set: UP (default) or DOWN
    """

def selection_set_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add new Selection Set(s) from the clipboard"""

def selection_set_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove a Selection Set from this Armature"""

def selection_set_remove_bones(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the selected bones from all Selection Sets"""

def selection_set_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    selection_set_index: int | None = -1,
) -> None:
    """Select the bones from this Selection Set

    :param selection_set_index: Selection Set Index, Which Selection Set to select; -1 uses the active Selection Set
    """

def selection_set_unassign(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected bones from Selection Set"""

def transforms_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset location, rotation, and scaling of selected bones to their default values"""

def user_transforms_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_selected: bool | None = True,
) -> None:
    """Reset pose bone transforms to keyframed state

    :param only_selected: Only Selected, Only visible/selected bones
    """

def visual_transform_apply(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Apply final constrained position of pose bones to their transform"""
