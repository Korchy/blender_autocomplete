import typing
import collections.abc
import typing_extensions
import bpy.ops.transform
import bpy.types
import bpy.typing

def action_pushdown(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    track_index: int | None = -1,
):
    """Push action down onto the top of the NLA stack as a new strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param track_index: Track Index, Index of NLA action track to perform pushdown operation on
    :type track_index: int | None
    """

def action_sync_length(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    active: bool | None = True,
):
    """Synchronize the length of the referenced Action with the length used in the strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param active: Active Strip Only, Only sync the active length for the active strip
    :type active: bool | None
    """

def action_unlink(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    force_delete: bool | None = False,
):
    """Unlink this action from the active action slot (and/or exit Tweak Mode)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-block's NLA stack
    :type force_delete: bool | None
    """

def actionclip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "",
):
    """Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param action: Action
    :type action: str | None
    """

def apply_scale(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply scaling of selected strips to their referenced Actions

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def bake(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
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
):
    """Bake all selected objects location/scale/rotation animation to an action

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param frame_start: Start Frame, Start frame for baking
        :type frame_start: int | None
        :param frame_end: End Frame, End frame for baking
        :type frame_end: int | None
        :param step: Frame Step, Number of frames to skip forward while baking each frame
        :type step: int | None
        :param only_selected: Only Selected Bones, Only key selected bones (Pose baking only)
        :type only_selected: bool | None
        :param visual_keying: Visual Keying, Keyframe from the final transformations (with constraints applied)
        :type visual_keying: bool | None
        :param clear_constraints: Clear Constraints, Remove all constraints from keyed object/bones, and do 'visual' keying
        :type clear_constraints: bool | None
        :param clear_parents: Clear Parents, Bake animation onto the object then clear parents (objects only)
        :type clear_parents: bool | None
        :param use_current_action: Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature)
        :type use_current_action: bool | None
        :param clean_curves: Clean Curves, After baking curves, remove redundant keys
        :type clean_curves: bool | None
        :param bake_types: Bake Data, Which data's transformations to bake

    POSE
    Pose -- Bake bones transformations.

    OBJECT
    Object -- Bake object transformations.
        :type bake_types: set[typing.Literal['POSE','OBJECT']] | None
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
        :type channel_types: set[typing.Literal['LOCATION','ROTATION','SCALE','BBONE','PROPS']] | None
    """

def channels_click(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | None = False,
):
    """Handle clicks to select NLA tracks

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend Select
    :type extend: bool | None
    """

def clear_scale(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset scaling of selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def click_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    wait_to_deselect_others: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    deselect_all: bool | None = False,
):
    """Handle clicks to select NLA Strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: bool | None
    :param mouse_x: Mouse X
    :type mouse_x: int | None
    :param mouse_y: Mouse Y
    :type mouse_y: int | None
    :param extend: Extend Select
    :type extend: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    """

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    linked: bool | None = False,
):
    """Duplicate selected NLA-Strips, adding the new strips to new track(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param linked: Linked, When duplicating strips, assign new copies of the actions they use
    :type linked: bool | None
    """

def duplicate_linked_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    NLA_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Duplicate Linked selected NLA-Strips, adding the new strips to new track(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)
    :type NLA_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    NLA_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Duplicate selected NLA-Strips, adding the new strips to new track(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)
    :type NLA_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def fmodifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: bpy.typing.FmodifierTypeItems | None = "NULL",
    only_active: bool | None = True,
):
    """Add F-Modifier to the active/selected NLA-Strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.typing.FmodifierTypeItems | None
    :param only_active: Only Active, Only add a F-Modifier of the specified type to the active strip
    :type only_active: bool | None
    """

def fmodifier_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the F-Modifier(s) of the active NLA-Strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def fmodifier_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_active: bool | None = True,
    replace: bool | None = False,
):
    """Add copied F-Modifiers to the selected NLA-Strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Only Active, Only paste F-Modifiers on active strip
    :type only_active: bool | None
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
    :type replace: bool | None
    """

def make_single_user(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    confirm: bool | None = True,
):
    """Make linked action local to each strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
    """

def meta_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add new meta-strips incorporating the selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def meta_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Separate out the strips held by the selected meta-strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def move_down(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Move selected strips down a track if there's room

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def move_up(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Move selected strips up a track if there's room

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mute_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Mute or un-mute selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def previewrange_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set Preview Range based on extends of selected strips

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
    """Select or deselect all NLA-Strips

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
    tweak: bool | None = False,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
):
    """Use box selection to grab NLA-Strips

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param axis_range: Axis Range
        :type axis_range: bool | None
        :param tweak: Tweak, Operator has been activated using a click-drag event
        :type tweak: bool | None
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

def select_leftright(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal["CHECK", "LEFT", "RIGHT"] | None = "CHECK",
    extend: bool | None = False,
):
    """Select strips to the left or the right of the current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['CHECK','LEFT','RIGHT'] | None
    :param extend: Extend Select
    :type extend: bool | None
    """

def selected_objects_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make selected objects appear in NLA Editor by adding Animation Data

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: typing.Literal["CFRA", "NEAREST_FRAME", "NEAREST_SECOND", "NEAREST_MARKER"]
    | None = "CFRA",
):
    """Move start of strips to specified time

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['CFRA','NEAREST_FRAME','NEAREST_SECOND','NEAREST_MARKER'] | None
    """

def soundclip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a strip for controlling when speaker plays its sound clip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def split(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Split selected strips at their midpoints

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def swap(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Swap order of selected strips within tracks

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def tracks_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    above_selected: bool | None = False,
):
    """Add NLA-Tracks above/after the selected tracks

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param above_selected: Above Selected, Add a new NLA Track above every existing selected one
    :type above_selected: bool | None
    """

def tracks_delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete selected NLA-Tracks and the strips they contain

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def transition_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a transition strip between two adjacent selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def tweakmode_enter(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    isolate_action: bool | None = False,
    use_upper_stack_evaluation: bool | None = False,
):
    """Enter tweaking mode for the action referenced by the active strip to edit its keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param isolate_action: Isolate Action, Enable 'solo' on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack
    :type isolate_action: bool | None
    :param use_upper_stack_evaluation: Evaluate Upper Stack, In tweak mode, display the effects of the tracks above the tweak strip
    :type use_upper_stack_evaluation: bool | None
    """

def tweakmode_exit(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    isolate_action: bool | None = False,
):
    """Exit tweaking mode for the action referenced by the active strip

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param isolate_action: Isolate Action, Disable 'solo' on any of the NLA Tracks after exiting tweak mode to get things back to normal
    :type isolate_action: bool | None
    """

def view_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset viewable area to show full strips range

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
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
):
    """Reset viewable area to show selected strips range

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """
