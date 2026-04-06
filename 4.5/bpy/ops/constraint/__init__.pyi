import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def add_target(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a target to the constraint"""

def apply(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    report: bool | None = False,
) -> None:
    """Apply constraint and remove from the stack

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :param report: Report, Create a notification after the operation
    """

def childof_clear_inverse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
) -> None:
    """Clear inverse correction for Child Of constraint

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
    """

def childof_set_inverse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
) -> None:
    """Set inverse correction for Child Of constraint

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
    """

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    report: bool | None = False,
) -> None:
    """Duplicate constraint at the same position in the stack

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :param report: Report, Create a notification after the operation
    """

def copy_to_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
) -> None:
    """Copy constraint to other selected objects/bones

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    report: bool | None = False,
) -> None:
    """Remove constraint from constraint stack

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :param report: Report, Create a notification after the operation
    """

def disable_keep_transform(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the influence of this constraint to zero while trying to maintain the objects transformation. Other active constraints can still influence the final transformation"""

def followpath_path_animate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    frame_start: int | None = 1,
    length: int | None = 100,
) -> None:
    """Add default animation for path used by constraint if it isnt animated already

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :param frame_start: Start Frame, First frame of path animation
        :param length: Length, Number of frames that path animation should take
    """

def limitdistance_reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
) -> None:
    """Reset limiting distance for Limit Distance Constraint

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
    """

def move_down(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
) -> None:
    """Move constraint down in constraint stack

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
    """

def move_to_index(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    index: int | None = 0,
) -> None:
    """Change the constraints position in the list so it evaluates after the set number of others

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
        :param index: Index, The index to move the constraint to
    """

def move_up(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
) -> None:
    """Move constraint up in constraint stack

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
    """

def normalize_target_weights(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Normalize weights of all target bones"""

def objectsolver_clear_inverse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
) -> None:
    """Clear inverse correction for Object Solver constraint

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
    """

def objectsolver_set_inverse(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
) -> None:
    """Set inverse correction for Object Solver constraint

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
    """

def remove_target(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Remove the target from the constraint

    :param index: index
    """

def stretchto_reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
) -> None:
    """Reset original length of bone for Stretch To Constraint

        :param constraint: Constraint, Name of the constraint to edit
        :param owner: Owner, The owner of this constraint

    OBJECT
    Object -- Edit a constraint on the active object.

    BONE
    Bone -- Edit a constraint on the active bone.
    """
