import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def add_target(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a target to the constraint :File: `startup/bl_operators/constraint.py\:26 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L26>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def apply(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          constraint: typing.Union[str, typing.Any] = "",
          owner: typing.Optional[typing.Any] = 'OBJECT',
          report: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Apply constraint and remove from the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    :param report: Report, Create a notification after the operation
    :type report: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def childof_clear_inverse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Clear inverse correction for Child Of constraint

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def childof_set_inverse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Set inverse correction for Child Of constraint

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def copy(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         constraint: typing.Union[str, typing.Any] = "",
         owner: typing.Optional[typing.Any] = 'OBJECT',
         report: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Duplicate constraint at the same position in the stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    :param report: Report, Create a notification after the operation
    :type report: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def copy_to_selected(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Copy constraint to other selected objects/bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def delete(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           constraint: typing.Union[str, typing.Any] = "",
           owner: typing.Optional[typing.Any] = 'OBJECT',
           report: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Remove constraint from constraint stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    :param report: Report, Create a notification after the operation
    :type report: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def disable_keep_transform(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set the influence of this constraint to zero while trying to maintain the object's transformation. Other active constraints can still influence the final transformation :File: `startup/bl_operators/constraint.py\:86 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L86>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def followpath_path_animate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT',
        frame_start: typing.Optional[typing.Any] = 1,
        length: typing.Optional[typing.Any] = 100):
    ''' Add default animation for path used by constraint if it isn't animated already

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    :param frame_start: Start Frame, First frame of path animation
    :type frame_start: typing.Optional[typing.Any]
    :param length: Length, Number of frames that path animation should take
    :type length: typing.Optional[typing.Any]
    '''

    pass


def limitdistance_reset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Reset limiting distance for Limit Distance Constraint

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def move_down(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Move constraint down in constraint stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def move_to_index(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT',
        index: typing.Optional[typing.Any] = 0):
    ''' Change the constraint's position in the list so it evaluates after the set number of others

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    :param index: Index, The index to move the constraint to
    :type index: typing.Optional[typing.Any]
    '''

    pass


def move_up(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
            execution_context: typing.Optional[typing.Union[str, int]] = None,
            undo: typing.Optional[bool] = None,
            *,
            constraint: typing.Union[str, typing.Any] = "",
            owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Move constraint up in constraint stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def normalize_target_weights(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Normalize weights of all target bones :File: `startup/bl_operators/constraint.py\:61 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L61>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def objectsolver_clear_inverse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Clear inverse correction for Object Solver constraint

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def objectsolver_set_inverse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Set inverse correction for Object Solver constraint

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def remove_target(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        index: typing.Optional[typing.Any] = 0):
    ''' Remove the target from the constraint :File: `startup/bl_operators/constraint.py\:44 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L44>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param index: index
    :type index: typing.Optional[typing.Any]
    '''

    pass


def stretchto_reset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Reset original length of bone for Stretch To Constraint

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object -- Edit a constraint on the active object. * ``BONE`` Bone -- Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass
