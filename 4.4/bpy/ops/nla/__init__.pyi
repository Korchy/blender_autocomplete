import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums

def action_pushdown(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    track_index: int | None = -1,
) -> None:
    """Push action down onto the top of the NLA stack as a new strip

    :param track_index: Track Index, Index of NLA action track to perform pushdown operation on
    """

def action_sync_length(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    active: bool | None = True,
) -> None:
    """Synchronize the length of the referenced Action with the length used in the strip

    :param active: Active Strip Only, Only sync the active length for the active strip
    """

def action_unlink(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    force_delete: bool | None = False,
) -> None:
    """Unlink this action from the active action slot (and/or exit Tweak Mode)

    :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-blocks NLA stack
    """

def actionclip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: str | None = "",
) -> None:
    """Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track

    :param action: Action
    """

def apply_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Apply scaling of selected strips to their referenced Actions"""

def bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_start: int | None = 1,
    frame_end: int | None = 250,
    step: int | None = 1,
    only_selected: bool | None = True,
    visual_keying: bool | None = False,
    clear_constraints: bool | None = False,
    clear_parents: bool | None = False,
    use_current_action: bool | None = False,
    clean_curves: bool | None = False,
    bake_types: set[typing.Literal["POSE", "OBJECT"]] | None = {"POSE"},
    channel_types: set[
        typing.Literal["LOCATION", "ROTATION", "SCALE", "BBONE", "PROPS"]
    ]
    | None = {"BBONE", "LOCATION", "PROPS", "ROTATION", "SCALE"},
) -> None:
    """Bake all selected objects location/scale/rotation animation to an action

        :param frame_start: Start Frame, Start frame for baking
        :param frame_end: End Frame, End frame for baking
        :param step: Frame Step, Number of frames to skip forward while baking each frame
        :param only_selected: Only Selected Bones, Only key selected bones (Pose baking only)
        :param visual_keying: Visual Keying, Keyframe from the final transformations (with constraints applied)
        :param clear_constraints: Clear Constraints, Remove all constraints from keyed object/bones. To get a correct bake with this setting Visual Keying should be enabled
        :param clear_parents: Clear Parents, Bake animation onto the object then clear parents (objects only)
        :param use_current_action: Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature)
        :param clean_curves: Clean Curves, After baking curves, remove redundant keys
        :param bake_types: Bake Data, Which datas transformations to bake

    POSE
    Pose -- Bake bones transformations.

    OBJECT
    Object -- Bake object transformations.
        :param channel_types: Channels, Which channels to bake

    LOCATION
    Location -- Bake location channels.

    ROTATION
    Rotation -- Bake rotation channels.

    SCALE
    Scale -- Bake scale channels.

    BBONE
    B-Bone -- Bake B-Bone channels.

    PROPS
    Custom Properties -- Bake custom properties.
    """

def channels_click(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Handle clicks to select NLA tracks

    :param extend: Extend Select
    """

def clear_scale(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset scaling of selected strips"""

def click_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    deselect_all: bool | None = False,
) -> None:
    """Handle clicks to select NLA Strips

    :param wait_to_deselect_others: Wait to Deselect Others
    :param mouse_x: Mouse X
    :param mouse_y: Mouse Y
    :param extend: Extend Select
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete selected strips"""

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    linked: bool | None = False,
) -> None:
    """Duplicate selected NLA-Strips, adding the new strips to new track(s)

    :param linked: Linked, When duplicating strips, assign new copies of the actions they use
    """

def duplicate_linked_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NLA_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate Linked selected NLA-Strips, adding the new strips to new track(s)

    :param NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    NLA_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate selected NLA-Strips, adding the new strips to new track(s)

    :param NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def fmodifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.FmodifierTypeItems | None = "NULL",
    only_active: bool | None = True,
) -> None:
    """Add F-Modifier to the active/selected NLA-Strips

    :param type: Type
    :param only_active: Only Active, Only add a F-Modifier of the specified type to the active strip
    """

def fmodifier_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the F-Modifier(s) of the active NLA-Strip"""

def fmodifier_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_active: bool | None = True,
    replace: bool | None = False,
) -> None:
    """Add copied F-Modifiers to the selected NLA-Strips

    :param only_active: Only Active, Only paste F-Modifiers on active strip
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
    """

def make_single_user(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Make linked action local to each strip

    :param confirm: Confirm, Prompt for confirmation
    """

def meta_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add new meta-strips incorporating the selected strips"""

def meta_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Separate out the strips held by the selected meta-strips"""

def move_down(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move selected strips down a track if theres room"""

def move_up(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move selected strips up a track if theres room"""

def mute_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Mute or un-mute selected strips"""

def previewrange_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set Preview Range based on extends of selected strips"""

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Select or deselect all NLA-Strips

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
    tweak: bool | None = False,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Use box selection to grab NLA-Strips

        :param axis_range: Axis Range
        :param tweak: Tweak, Operator has been activated using a click-drag event
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

def select_leftright(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["CHECK", "LEFT", "RIGHT"] | None = "CHECK",
    extend: bool | None = False,
) -> None:
    """Select strips to the left or the right of the current frame

    :param mode: Mode
    :param extend: Extend Select
    """

def selected_objects_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Make selected objects appear in NLA Editor by adding Animation Data"""

def snap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CFRA", "NEAREST_FRAME", "NEAREST_SECOND", "NEAREST_MARKER"]
    | None = "CFRA",
) -> None:
    """Move start of strips to specified time

    :param type: Type
    """

def soundclip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a strip for controlling when speaker plays its sound clip"""

def split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Split selected strips at their midpoints"""

def swap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Swap order of selected strips within tracks"""

def tracks_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    above_selected: bool | None = False,
) -> None:
    """Add NLA-Tracks above/after the selected tracks

    :param above_selected: Above Selected, Add a new NLA Track above every existing selected one
    """

def tracks_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete selected NLA-Tracks and the strips they contain"""

def transition_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a transition strip between two adjacent selected strips"""

def tweakmode_enter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    isolate_action: bool | None = False,
    use_upper_stack_evaluation: bool | None = False,
) -> None:
    """Enter tweaking mode for the action referenced by the active strip to edit its keyframes

    :param isolate_action: Isolate Action, Enable solo on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack
    :param use_upper_stack_evaluation: Evaluate Upper Stack, In tweak mode, display the effects of the tracks above the tweak strip
    """

def tweakmode_exit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    isolate_action: bool | None = False,
) -> None:
    """Exit tweaking mode for the action referenced by the active strip

    :param isolate_action: Isolate Action, Disable solo on any of the NLA Tracks after exiting tweak mode to get things back to normal
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset viewable area to show full strips range"""

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
    """Reset viewable area to show selected strips range"""
