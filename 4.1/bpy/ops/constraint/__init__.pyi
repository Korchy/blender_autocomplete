import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def add_target(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a target to the constraint

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def apply(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
    report: bool | typing.Any | None = False,
):
    """Apply constraint and remove from the stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
        :param report: Report, Create a notification after the operation
        :type report: bool | typing.Any | None
    """

    ...

def childof_clear_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Clear inverse correction for Child Of constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def childof_set_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Set inverse correction for Child Of constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
    report: bool | typing.Any | None = False,
):
    """Duplicate constraint at the same position in the stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
        :param report: Report, Create a notification after the operation
        :type report: bool | typing.Any | None
    """

    ...

def copy_to_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Copy constraint to other selected objects/bones

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
    report: bool | typing.Any | None = False,
):
    """Remove constraint from constraint stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
        :param report: Report, Create a notification after the operation
        :type report: bool | typing.Any | None
    """

    ...

def disable_keep_transform(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set the influence of this constraint to zero while trying to maintain the object's transformation. Other active constraints can still influence the final transformation

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def followpath_path_animate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
    frame_start: typing.Any | None = 1,
    length: typing.Any | None = 100,
):
    """Add default animation for path used by constraint if it isn't animated already

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
        :param frame_start: Start Frame, First frame of path animation
        :type frame_start: typing.Any | None
        :param length: Length, Number of frames that path animation should take
        :type length: typing.Any | None
    """

    ...

def limitdistance_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Reset limiting distance for Limit Distance Constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def move_down(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Move constraint down in constraint stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def move_to_index(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
    index: typing.Any | None = 0,
):
    """Change the constraint's position in the list so it evaluates after the set number of others

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
        :param index: Index, The index to move the constraint to
        :type index: typing.Any | None
    """

    ...

def move_up(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Move constraint up in constraint stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def normalize_target_weights(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Normalize weights of all target bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def objectsolver_clear_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Clear inverse correction for Object Solver constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def objectsolver_set_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Set inverse correction for Object Solver constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def remove_target(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
):
    """Remove the target from the constraint

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: index
    :type index: typing.Any | None
    """

    ...

def stretchto_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Reset original length of bone for Stretch To Constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...
