import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class action_pushdown(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        track_index: int | None = -1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Push action down onto the top of the NLA stack as a new strip

        :param execution_context:
        :param undo:
        :param track_index: Track Index, Index of NLA action track to perform pushdown operation on (in [-1, inf], optional)
        :return: Result of the operator call.
        """

class action_sync_length(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        active: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Synchronize the length of the referenced Action with the length used in the strip

        :param execution_context:
        :param undo:
        :param active: Active Strip Only, Only sync the active length for the active strip (optional)
        :return: Result of the operator call.
        """

class action_unlink(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        force_delete: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unlink this action from the active action slot (and/or exit Tweak Mode)

        :param execution_context:
        :param undo:
        :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-blocks NLA stack (optional)
        :return: Result of the operator call.
        """

class actionclip_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: str | None = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track

        :param execution_context:
        :param undo:
        :param action: Action, (optional)
        :return: Result of the operator call.
        """

class apply_scale(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply scaling of selected strips to their referenced Actions

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class bake(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Bake all selected objects location/scale/rotation animation to an action

                :param execution_context:
                :param undo:
                :param frame_start: Start Frame, Start frame for baking (in [0, 300000], optional)
                :param frame_end: End Frame, End frame for baking (in [1, 300000], optional)
                :param step: Frame Step, Number of frames to skip forward while baking each frame (in [1, 120], optional)
                :param only_selected: Only Selected Bones, Only key selected bones (Pose baking only) (optional)
                :param visual_keying: Visual Keying, Keyframe from the final transformations (with constraints applied) (optional)
                :param clear_constraints: Clear Local Constraints, Remove all constraints from keyed object/bones. To get a correct bake with this setting Visual Keying should be enabled (optional)
                :param clear_parents: Clear Parents, Bake animation onto the object then clear parents (objects only) (optional)
                :param use_current_action: Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature) (optional)
                :param clean_curves: Clean Curves, After baking curves, remove redundant keys (optional)
                :param bake_types: Bake Data, Which datas transformations to bake (optional)

        POSE
        Pose -- Bake bones transformations.

        OBJECT
        Object -- Bake object transformations.
                :param channel_types: Channels, Which channels to bake (optional)

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
                :return: Result of the operator call.
        """

class channels_click(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Handle clicks to select NLA tracks

        :param execution_context:
        :param undo:
        :param extend: Extend Select, (optional)
        :return: Result of the operator call.
        """

class clear_scale(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset scaling of selected strips

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class click_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Handle clicks to select NLA Strips

        :param execution_context:
        :param undo:
        :param wait_to_deselect_others: Wait to Deselect Others, (optional)
        :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if theres drag event. Otherwise select on mouse release (optional)
        :param mouse_x: Mouse X, (in [-inf, inf], optional)
        :param mouse_y: Mouse Y, (in [-inf, inf], optional)
        :param extend: Extend Select, (optional)
        :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor (optional)
        :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete selected strips

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class duplicate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        linked: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate selected NLA-Strips, adding the new strips to new track(s)

        :param execution_context:
        :param undo:
        :param linked: Linked, When duplicating strips, assign new copies of the actions they use (optional)
        :return: Result of the operator call.
        """

class duplicate_linked_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        NLA_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate Linked selected NLA-Strips, adding the new strips to new track(s)

        :param execution_context:
        :param undo:
        :param NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s) (optional, `bpy.ops.nla.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class duplicate_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        NLA_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate selected NLA-Strips, adding the new strips to new track(s)

        :param execution_context:
        :param undo:
        :param NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s) (optional, `bpy.ops.nla.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class fmodifier_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[bpy.stub_internal.rna_enums.FmodifierTypeItems]
        | None = "NULL",
        only_active: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add F-Modifier to the active/selected NLA-Strips

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param only_active: Only Active, Only add a F-Modifier of the specified type to the active strip (optional)
        :return: Result of the operator call.
        """

class fmodifier_copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the F-Modifier(s) of the active NLA-Strip

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class fmodifier_paste(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        only_active: bool | None = True,
        replace: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add copied F-Modifiers to the selected NLA-Strips

        :param execution_context:
        :param undo:
        :param only_active: Only Active, Only paste F-Modifiers on active strip (optional)
        :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list (optional)
        :return: Result of the operator call.
        """

class make_single_user(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        confirm: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make linked action local to each strip

        :param execution_context:
        :param undo:
        :param confirm: Confirm, Prompt for confirmation (optional)
        :return: Result of the operator call.
        """

class meta_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add new meta-strips incorporating the selected strips

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class meta_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Separate out the strips held by the selected meta-strips

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class move_down(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move selected strips down a track if theres room

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class move_up(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move selected strips up a track if theres room

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class mute_toggle(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mute or un-mute selected strips

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class previewrange_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set Preview Range based on extents of selected strips

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"]
        | None = "TOGGLE",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select or deselect all NLA-Strips

                :param execution_context:
                :param undo:
                :param action: Action, Selection action to execute (optional)

        TOGGLE
        Toggle -- Toggle selection for all elements.

        SELECT
        Select -- Select all elements.

        DESELECT
        Deselect -- Deselect all elements.

        INVERT
        Invert -- Invert selection of all elements.
                :return: Result of the operator call.
        """

class select_box(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
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
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Use box selection to grab NLA-Strips

                :param execution_context:
                :param undo:
                :param axis_range: Axis Range, (optional)
                :param tweak: Tweak, Operator has been activated using a click-drag event (optional)
                :param xmin: X Min, (in [-inf, inf], optional)
                :param xmax: X Max, (in [-inf, inf], optional)
                :param ymin: Y Min, (in [-inf, inf], optional)
                :param ymax: Y Max, (in [-inf, inf], optional)
                :param wait_for_input: Wait for Input, (optional)
                :param mode: Mode, (optional)

        SET
        Set -- Set a new selection.

        ADD
        Extend -- Extend existing selection.

        SUB
        Subtract -- Subtract existing selection.
                :return: Result of the operator call.
        """

class select_leftright(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["CHECK", "LEFT", "RIGHT"] | None = "CHECK",
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select strips to the left or the right of the current frame

        :param execution_context:
        :param undo:
        :param mode: Mode, (optional)
        :param extend: Extend Select, (optional)
        :return: Result of the operator call.
        """

class selected_objects_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make selected objects appear in NLA Editor by adding Animation Data

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class snap(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "CFRA", "NEAREST_FRAME", "NEAREST_SECOND", "NEAREST_MARKER"
        ]
        | None = "CFRA",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move start of strips to specified time

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :return: Result of the operator call.
        """

class soundclip_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a strip for controlling when speaker plays its sound clip

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class split(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Split selected strips at their midpoints

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class swap(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Swap order of selected strips within tracks

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class tracks_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        above_selected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add NLA-Tracks above/after the selected tracks

        :param execution_context:
        :param undo:
        :param above_selected: Above Selected, Add a new NLA Track above every existing selected one (optional)
        :return: Result of the operator call.
        """

class tracks_delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete selected NLA-Tracks and the strips they contain

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class transition_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a transition strip between two adjacent selected strips

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class tweakmode_enter(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        isolate_action: bool | None = False,
        use_upper_stack_evaluation: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enter tweaking mode for the action referenced by the active strip to edit its keyframes

        :param execution_context:
        :param undo:
        :param isolate_action: Isolate Action, Enable solo on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack (optional)
        :param use_upper_stack_evaluation: Evaluate Upper Stack, In tweak mode, display the effects of the tracks above the tweak strip (optional)
        :return: Result of the operator call.
        """

class tweakmode_exit(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        isolate_action: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Exit tweaking mode for the action referenced by the active strip

        :param execution_context:
        :param undo:
        :param isolate_action: Isolate Action, Disable solo on any of the NLA Tracks after exiting tweak mode to get things back to normal (optional)
        :return: Result of the operator call.
        """

class view_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset viewable area to show full strips range

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_frame(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move the view to the current frame

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class view_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset viewable area to show selected strips range

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
