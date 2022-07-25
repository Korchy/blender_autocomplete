import sys
import typing


def add_target():
    ''' Add a target to the constraint :file: startup/bl_operators/constraint.py\:41 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/constraint.py$41> _

    '''

    pass


def apply(constraint: str = "",
          owner: typing.Union[str, int] = 'OBJECT',
          report: bool = False):
    ''' Apply constraint and remove from the stack

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def childof_clear_inverse(constraint: str = "",
                          owner: typing.Union[str, int] = 'OBJECT'):
    ''' Clear inverse correction for Child Of constraint

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def childof_set_inverse(constraint: str = "",
                        owner: typing.Union[str, int] = 'OBJECT'):
    ''' Set inverse correction for Child Of constraint

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def copy(constraint: str = "",
         owner: typing.Union[str, int] = 'OBJECT',
         report: bool = False):
    ''' Duplicate constraint at the same position in the stack

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def copy_to_selected(constraint: str = "",
                     owner: typing.Union[str, int] = 'OBJECT'):
    ''' Copy constraint to other selected objects/bones

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def delete(constraint: str = "",
           owner: typing.Union[str, int] = 'OBJECT',
           report: bool = False):
    ''' Remove constraint from constraint stack

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param report: Report, Create a notification after the operation
    :type report: bool
    '''

    pass


def disable_keep_transform():
    ''' Set the influence of this constraint to zero while trying to maintain the object's transformation. Other active constraints can still influence the final transformation :file: startup/bl_operators/constraint.py\:101 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/constraint.py$101> _

    '''

    pass


def followpath_path_animate(constraint: str = "",
                            owner: typing.Union[str, int] = 'OBJECT',
                            frame_start: int = 1,
                            length: int = 100):
    ''' Add default animation for path used by constraint if it isn't animated already

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


def limitdistance_reset(constraint: str = "",
                        owner: typing.Union[str, int] = 'OBJECT'):
    ''' Reset limiting distance for Limit Distance Constraint

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def move_down(constraint: str = "", owner: typing.Union[str, int] = 'OBJECT'):
    ''' Move constraint down in constraint stack

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def move_to_index(constraint: str = "",
                  owner: typing.Union[str, int] = 'OBJECT',
                  index: int = 0):
    ''' Change the constraint's position in the list so it evaluates after the set number of others

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    :param index: Index, The index to move the constraint to
    :type index: int
    '''

    pass


def move_up(constraint: str = "", owner: typing.Union[str, int] = 'OBJECT'):
    ''' Move constraint up in constraint stack

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def normalize_target_weights():
    ''' Normalize weights of all target bones :file: startup/bl_operators/constraint.py\:76 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/constraint.py$76> _

    '''

    pass


def objectsolver_clear_inverse(constraint: str = "",
                               owner: typing.Union[str, int] = 'OBJECT'):
    ''' Clear inverse correction for Object Solver constraint

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def objectsolver_set_inverse(constraint: str = "",
                             owner: typing.Union[str, int] = 'OBJECT'):
    ''' Set inverse correction for Object Solver constraint

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass


def remove_target(index: int = 0):
    ''' Remove the target from the constraint

    :param index: index
    :type index: int
    '''

    pass


def stretchto_reset(constraint: str = "",
                    owner: typing.Union[str, int] = 'OBJECT'):
    ''' Reset original length of bone for Stretch To Constraint

    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: str
    :param owner: Owner, The owner of this constraint * OBJECT Object -- Edit a constraint on the active object. * BONE Bone -- Edit a constraint on the active bone.
    :type owner: typing.Union[str, int]
    '''

    pass
