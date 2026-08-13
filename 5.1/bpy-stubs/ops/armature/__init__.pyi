import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class align(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Align selected bones to the active bone (or to their parent)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class assign_to_collection(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection_index: int | None = -1,
        new_collection_name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Assign all selected bones to a collection, or unassign them, depending on whether the active bone is already assigned or not

        :param execution_context:
        :param undo:
        :param collection_index: Collection Index, Index of the collection to assign selected bones to. When the operator should create a new bone collection, use new_collection_name to define the collection name, and set this parameter to the parent index of the new bone collection (in [-1, inf], optional)
        :param new_collection_name: Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and assign the selected bones to it. To assign to an existing collection, do not include this parameter and use collection_index (optional, never None)
        :return: Result of the operator call.
        """

class autoside_names(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["XAXIS", "YAXIS", "ZAXIS"] | None = "XAXIS",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Automatically renames the selected bones according to which side of the target axis they fall on

                :param execution_context:
                :param undo:
                :param type: Axis, Axis to tag names with (optional)

        XAXIS
        X-Axis -- Left/Right.

        YAXIS
        Y-Axis -- Front/Back.

        ZAXIS
        Z-Axis -- Top/Bottom.
                :return: Result of the operator call.
        """

class bone_primitive_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "Bone",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new bone located at the 3D cursor

        :param execution_context:
        :param undo:
        :param name: Name, Name of the newly created bone (optional, never None)
        :return: Result of the operator call.
        """

class calculate_roll(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "POS_X",
            "POS_Z",
            "GLOBAL_POS_X",
            "GLOBAL_POS_Y",
            "GLOBAL_POS_Z",
            "NEG_X",
            "NEG_Z",
            "GLOBAL_NEG_X",
            "GLOBAL_NEG_Y",
            "GLOBAL_NEG_Z",
            "ACTIVE",
            "VIEW",
            "CURSOR",
        ]
        | None = "POS_X",
        axis_flip: bool | None = False,
        axis_only: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Automatically fix alignment of select bones axes

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param axis_flip: Flip Axis, Negate the alignment axis (optional)
        :param axis_only: Shortest Rotation, Ignore the axis direction, use the shortest rotation to align (optional)
        :return: Result of the operator call.
        """

class click_extrude(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new bone going from the last selected joint to the mouse position

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_add(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a new bone collection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_assign(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add selected bones to the chosen bone collection

        :param execution_context:
        :param undo:
        :param name: Bone Collection, Name of the bone collection to assign this bone to; empty to assign to the active bone collection (optional, never None)
        :return: Result of the operator call.
        """

class collection_create_and_assign(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new bone collection and assign all selected bones

        :param execution_context:
        :param undo:
        :param name: Bone Collection, Name of the bone collection to create (optional, never None)
        :return: Result of the operator call.
        """

class collection_deselect(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect bones of active Bone Collection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["UP", "DOWN"] | None = "UP",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change position of active Bone Collection in list of Bone collections

        :param execution_context:
        :param undo:
        :param direction: Direction, Direction to move the active Bone Collection towards (optional)
        :return: Result of the operator call.
        """

class collection_remove(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the active bone collection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_remove_unused(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove all bone collections that have neither bones nor children. This is done recursively, so bone collections that only have unused children are also removed

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_select(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select bones in active Bone Collection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_show_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Show all bone collections

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class collection_unassign(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove selected bones from the active bone collection

        :param execution_context:
        :param undo:
        :param name: Bone Collection, Name of the bone collection to unassign this bone from; empty to unassign from the active bone collection (optional, never None)
        :return: Result of the operator call.
        """

class collection_unassign_named(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        name: str = "",
        bone_name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Unassign the named bone from this bone collection

        :param execution_context:
        :param undo:
        :param name: Bone Collection, Name of the bone collection to unassign this bone from; empty to unassign from the active bone collection (optional, never None)
        :param bone_name: Bone Name, Name of the bone to unassign from the collection; empty to use the active bone (optional, never None)
        :return: Result of the operator call.
        """

class collection_unsolo_all(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear the solo setting on all bone collections

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class copy_bone_color_to_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        bone_type: typing.Literal["EDIT", "POSE"] | None = "EDIT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy the bone color of the active bone to all selected bones

                :param execution_context:
                :param undo:
                :param bone_type: Type, (optional)

        EDIT
        Bone -- Copy Bone colors from the active bone to all selected bones.

        POSE
        Pose Bone -- Copy Pose Bone colors from the active pose bone to all selected pose bones.
                :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        confirm: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove selected bones from the armature

        :param execution_context:
        :param undo:
        :param confirm: Confirm, Prompt for confirmation (optional)
        :return: Result of the operator call.
        """

class dissolve(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Dissolve selected bones from the armature

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
        do_flip_names: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make copies of the selected bones within the same armature

        :param execution_context:
        :param undo:
        :param do_flip_names: Flip Names, Try to flip names of the bones, if possible, instead of adding a number extension (optional)
        :return: Result of the operator call.
        """

class duplicate_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        ARMATURE_OT_duplicate: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Make copies of the selected bones within the same armature and move them

        :param execution_context:
        :param undo:
        :param ARMATURE_OT_duplicate: Duplicate Selected Bone(s), Make copies of the selected bones within the same armature (optional, `bpy.ops.armature.duplicate` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class extrude(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        forked: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create new bones from the selected joints

        :param execution_context:
        :param undo:
        :param forked: Forked, (optional)
        :return: Result of the operator call.
        """

class extrude_forked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        ARMATURE_OT_extrude: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create new bones from the selected joints and move them

        :param execution_context:
        :param undo:
        :param ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints (optional, `bpy.ops.armature.extrude` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class extrude_move(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        ARMATURE_OT_extrude: dict[str, typing.Any] | None = {},
        TRANSFORM_OT_translate: dict[str, typing.Any] | None = {},
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create new bones from the selected joints and move them

        :param execution_context:
        :param undo:
        :param ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints (optional, `bpy.ops.armature.extrude` keyword arguments)
        :param TRANSFORM_OT_translate: Move, Move selected items (optional, `bpy.ops.transform.translate` keyword arguments)
        :return: Result of the operator call.
        """

class fill(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add bone between selected joint(s) and/or 3D cursor

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class flip_names(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        do_strip_numbers: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Flips (and corrects) the axis suffixes of the names of selected bones

        :param execution_context:
        :param undo:
        :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names.Warning: May result in incoherent naming in some cases(optional)
        :return: Result of the operator call.
        """

class hide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        unselected: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Tag selected bones to not be visible in Edit Mode

        :param execution_context:
        :param undo:
        :param unselected: Unselected, Hide unselected rather than selected (optional)
        :return: Result of the operator call.
        """

class move_to_collection(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        collection_index: int | None = -1,
        new_collection_name: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move bones to a collection

        :param execution_context:
        :param undo:
        :param collection_index: Collection Index, Index of the collection to move selected bones to. When the operator should create a new bone collection, do not include this parameter and pass new_collection_name (in [-1, inf], optional)
        :param new_collection_name: Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and move the selected bones to it. To move to an existing collection, do not include this parameter and use collection_index (optional, never None)
        :return: Result of the operator call.
        """

class parent_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["CLEAR", "DISCONNECT"] | None = "CLEAR",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the parent-child relationship between selected bones and their parents

        :param execution_context:
        :param undo:
        :param type: Clear Type, What way to clear parenting (optional)
        :return: Result of the operator call.
        """

class parent_set(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal["CONNECTED", "OFFSET"] | None = "CONNECTED",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the active bone as the parent of the selected bones

        :param execution_context:
        :param undo:
        :param type: Parent Type, Type of parenting (optional)
        :return: Result of the operator call.
        """

class reveal(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reveal all bones hidden in Edit Mode

        :param execution_context:
        :param undo:
        :param select: Select, (optional)
        :return: Result of the operator call.
        """

class roll_clear(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        roll: float | None = 0.0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear roll for selected bones

        :param execution_context:
        :param undo:
        :param roll: Roll, (in [-6.28319, 6.28319], optional)
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
        """Toggle selection status of all bones

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

class select_hierarchy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["PARENT", "CHILD"] | None = "PARENT",
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select immediate parent/children of selected bones

        :param execution_context:
        :param undo:
        :param direction: Direction, (optional)
        :param extend: Extend, Extend the selection (optional)
        :return: Result of the operator call.
        """

class select_less(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Deselect those bones at the boundary of each selection region

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_linked(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        all_forks: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select all bones linked by parent/child connections to the current selection

        :param execution_context:
        :param undo:
        :param all_forks: All Forks, Follow forks in the parents chain (optional)
        :return: Result of the operator call.
        """

class select_linked_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        deselect: bool | None = False,
        all_forks: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """(De)select bones linked by parent/child connections under the mouse cursor

        :param execution_context:
        :param undo:
        :param deselect: Deselect, (optional)
        :param all_forks: All Forks, Follow forks in the parents chain (optional)
        :return: Result of the operator call.
        """

class select_mirror(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        only_active: bool | None = False,
        extend: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Mirror the bone selection

        :param execution_context:
        :param undo:
        :param only_active: Active Only, Only operate on the active bone (optional)
        :param extend: Extend, Extend the selection (optional)
        :return: Result of the operator call.
        """

class select_more(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select those bones connected to the initial selection

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class select_similar(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        type: typing.Literal[
            "CHILDREN",
            "CHILDREN_IMMEDIATE",
            "SIBLINGS",
            "LENGTH",
            "DIRECTION",
            "PREFIX",
            "SUFFIX",
            "BONE_COLLECTION",
            "COLOR",
            "SHAPE",
        ]
        | None = "LENGTH",
        threshold: float | None = 0.1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select similar bones by property types

        :param execution_context:
        :param undo:
        :param type: Type, (optional)
        :param threshold: Threshold, (in [0, 1], optional)
        :return: Result of the operator call.
        """

class separate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Isolate selected bones into a separate armature

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class shortest_path_pick(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select shortest path between two bones

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
        """Split off selected bones from connected unselected bones

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class subdivide(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        number_cuts: int | None = 1,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Break selected bones into chains of smaller bones

        :param execution_context:
        :param undo:
        :param number_cuts: Number of Cuts, (in [1, 1000], optional)
        :return: Result of the operator call.
        """

class switch_direction(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the direction that a chain of bones points in (head and tail swap)

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class symmetrize(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        direction: typing.Literal["NEGATIVE_X", "POSITIVE_X"] | None = "NEGATIVE_X",
        copy_bone_colors: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Enforce symmetry, make copies of the selection or use existing

        :param execution_context:
        :param undo:
        :param direction: Direction, Which sides to copy from and to (when both are selected) (optional)
        :param copy_bone_colors: Bone Colors, Copy colors to existing bones (optional)
        :return: Result of the operator call.
        """
