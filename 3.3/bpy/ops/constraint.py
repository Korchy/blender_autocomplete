import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def add_target(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Add a target to the constraint :file: startup/bl_operators/constraint.py\:23 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/constraint.py$23> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def apply(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          constraint: str = "",
          owner: typing.Union[str, int] = 'OBJECT',
          report: bool = False):
    ''' Apply constraint and remove from the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def childof_clear_inverse(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None,
                          *,
                          constraint: str = "",
                          owner: typing.Union[str, int] = 'OBJECT'):
    ''' Clear inverse correction for Child Of constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def childof_set_inverse(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        constraint: str = "",
                        owner: typing.Union[str, int] = 'OBJECT'):
    ''' Set inverse correction for Child Of constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def copy(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         constraint: str = "",
         owner: typing.Union[str, int] = 'OBJECT',
         report: bool = False):
    ''' Duplicate constraint at the same position in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def copy_to_selected(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     constraint: str = "",
                     owner: typing.Union[str, int] = 'OBJECT'):
    ''' Copy constraint to other selected objects/bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           constraint: str = "",
           owner: typing.Union[str, int] = 'OBJECT',
           report: bool = False):
    ''' Remove constraint from constraint stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def disable_keep_transform(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None):
    ''' Set the influence of this constraint to zero while trying to maintain the object's transformation. Other active constraints can still influence the final transformation :file: startup/bl_operators/constraint.py\:83 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/constraint.py$83> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def followpath_path_animate(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            constraint: str = "",
                            owner: typing.Union[str, int] = 'OBJECT',
                            frame_start: int = 1,
                            length: int = 100):
    ''' Add default animation for path used by constraint if it isn't animated already

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param frame_start: Start Frame, First frame of path animation
    :type frame_start: int
    :param length: Length, Number of frames that path animation should take
    :type length: int
    '''

    pass


def limitdistance_reset(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None,
                        *,
                        constraint: str = "",
                        owner: typing.Union[str, int] = 'OBJECT'):
    ''' Reset limiting distance for Limit Distance Constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def move_down(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              constraint: str = "",
              owner: typing.Union[str, int] = 'OBJECT'):
    ''' Move constraint down in constraint stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def move_to_index(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  constraint: str = "",
                  owner: typing.Union[str, int] = 'OBJECT',
                  index: int = 0):
    ''' Change the constraint's position in the list so it evaluates after the set number of others

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param index: Index, The index to move the constraint to
    :type index: int
    '''

    pass


def move_up(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            constraint: str = "",
            owner: typing.Union[str, int] = 'OBJECT'):
    ''' Move constraint up in constraint stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def normalize_target_weights(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None):
    ''' Normalize weights of all target bones :file: startup/bl_operators/constraint.py\:58 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/constraint.py$58> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def objectsolver_clear_inverse(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        constraint: str = "",
        owner: typing.Union[str, int] = 'OBJECT'):
    ''' Clear inverse correction for Object Solver constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def objectsolver_set_inverse(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: bool = None,
                             *,
                             constraint: str = "",
                             owner: typing.Union[str, int] = 'OBJECT'):
    ''' Set inverse correction for Object Solver constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def remove_target(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  index: int = 0):
    ''' Remove the target from the constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param index: index
    :type index: int
    '''

    pass


def stretchto_reset(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    constraint: str = "",
                    owner: typing.Union[str, int] = 'OBJECT'):
    ''' Reset original length of bone for Stretch To Constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass
