import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class add_target(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add a target to the constraint

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class apply(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
        report: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply constraint and remove from the stack

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :param report: Report, Create a notification after the operation (optional)
                :return: Result of the operator call.
        """

class childof_clear_inverse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear inverse correction for Child Of constraint

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :return: Result of the operator call.
        """

class childof_set_inverse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set inverse correction for Child Of constraint

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :return: Result of the operator call.
        """

class copy(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
        report: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Duplicate constraint at the same position in the stack

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :param report: Report, Create a notification after the operation (optional)
                :return: Result of the operator call.
        """

class copy_to_selected(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Copy constraint to other selected objects/bones

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :return: Result of the operator call.
        """

class delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
        report: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove constraint from constraint stack

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :param report: Report, Create a notification after the operation (optional)
                :return: Result of the operator call.
        """

class disable_keep_transform(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set the influence of this constraint to zero while trying to maintain the objects transformation. Other active constraints can still influence the final transformation

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class followpath_path_animate(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
        frame_start: int | None = 1,
        length: int | None = 100,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Add default animation for path used by constraint if it isnt animated already

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :param frame_start: Start Frame, First frame of path animation (in [-1048574, 1048574], optional)
                :param length: Length, Number of frames that path animation should take (in [0, 1048574], optional)
                :return: Result of the operator call.
        """

class limitdistance_reset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset limiting distance for Limit Distance Constraint

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :return: Result of the operator call.
        """

class move_down(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move constraint down in constraint stack

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :return: Result of the operator call.
        """

class move_to_index(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Change the constraints position in the list so it evaluates after the set number of others

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :param index: Index, The index to move the constraint to (in [0, inf], optional)
                :return: Result of the operator call.
        """

class move_up(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Move constraint up in constraint stack

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :return: Result of the operator call.
        """

class normalize_target_weights(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Normalize weights of all target bones

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class objectsolver_clear_inverse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Clear inverse correction for Object Solver constraint

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :return: Result of the operator call.
        """

class objectsolver_set_inverse(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Set inverse correction for Object Solver constraint

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :return: Result of the operator call.
        """

class remove_target(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        index: int | None = 0,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Remove the target from the constraint

        :param execution_context:
        :param undo:
        :param index: index, (in [-inf, inf], optional)
        :return: Result of the operator call.
        """

class stretchto_reset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        constraint: str = "",
        owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Reset original length of bone for Stretch To Constraint

                :param execution_context:
                :param undo:
                :param constraint: Constraint, Name of the constraint to edit (optional, never None)
                :param owner: Owner, The owner of this constraint (optional)

        OBJECT
        Object -- Edit a constraint on the active object.

        BONE
        Bone -- Edit a constraint on the active bone.
                :return: Result of the operator call.
        """
