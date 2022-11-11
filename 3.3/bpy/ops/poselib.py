import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def action_sanitize(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None):
    ''' Deprecated, will be removed in Blender 3.3. Make action suitable for use as a Legacy Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def apply_pose(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               pose_index: int = -1):
    ''' Deprecated, will be removed in Blender 3.3. Apply specified Legacy Pose Library pose to the rig

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: int
    '''

    pass


def apply_pose_asset(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     blend_factor: float = 1.0,
                     flipped: bool = False):
    ''' Apply the given Pose Action to the rig

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses
    :type blend_factor: float
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: bool
    '''

    pass


def apply_pose_asset_for_keymap(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Apply the given Pose Action to the rig :file: addons/pose_library/operators.py\:431 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$431> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def blend_pose_asset(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     blend_factor: float = 0.0,
                     flipped: bool = False,
                     release_confirm: bool = False):
    ''' Blend the given Pose Action to the rig

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses
    :type blend_factor: float
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    '''

    pass


def blend_pose_asset_for_keymap(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Blend the given Pose Action to the rig :file: addons/pose_library/operators.py\:403 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$403> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def browse_interactive(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       pose_index: int = -1):
    ''' Deprecated, will be removed in Blender 3.3. Interactively browse Legacy Pose Library poses in 3D-View

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: int
    '''

    pass


def convert_old_object_poselib(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Create a pose asset for each pose marker in this legacy pose library data-block :file: addons/pose_library/operators.py\:487 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$487> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def convert_old_poselib(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Create a pose asset for each pose marker in the current action :file: addons/pose_library/operators.py\:453 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$453> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def copy_as_asset(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Create a new pose asset on the clipboard, to be pasted into an Asset Browser :file: addons/pose_library/operators.py\:210 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$210> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def create_pose_asset(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      pose_name: str = "",
                      activate_new_action: bool = True):
    ''' Create a new Action that contains the pose of the selected bones, and mark it as Asset. The asset will be stored in the current blend file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param pose_name: Pose Name
    :type pose_name: str
    :param activate_new_action: Activate New Action
    :type activate_new_action: bool
    '''

    pass


def new(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None):
    ''' Deprecated, will be removed in Blender 3.3. Add New Legacy Pose Library to active Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def paste_asset(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Paste the Asset that was previously copied using Copy As Asset :file: addons/pose_library/operators.py\:285 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$285> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def pose_add(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             frame: int = 1,
             name: str = "Pose"):
    ''' Deprecated, will be removed in Blender 3.3. Add the current Pose to the active Legacy Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame: Frame, Frame to store pose on
    :type frame: int
    :param name: Pose Name, Name of newly added Pose
    :type name: str
    '''

    pass


def pose_asset_select_bones(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None,
                            *,
                            select: bool = True,
                            flipped: bool = False):
    ''' Select those bones that are used in this pose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param select: Select
    :type select: bool
    :param flipped: Flipped
    :type flipped: bool
    '''

    pass


def pose_move(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              pose: typing.Union[str, int] = '',
              direction: typing.Union[str, int] = 'UP'):
    ''' Deprecated, will be removed in Blender 3.3. Move the pose up or down in the active Legacy Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param pose: Pose, The pose to move
    :type pose: typing.Union[str, int]
    :param direction: Direction, Direction to move the chosen pose towards
    :type direction: typing.Union[str, int]
    '''

    pass


def pose_remove(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                pose: typing.Union[str, int] = ''):
    ''' Deprecated, will be removed in Blender 3.3. Remove nth pose from the active Legacy Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param pose: Pose, The pose to remove
    :type pose: typing.Union[str, int]
    '''

    pass


def pose_rename(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                name: str = "RenamedPose",
                pose: typing.Union[str, int] = ''):
    ''' Deprecated, will be removed in Blender 3.3. Rename specified pose from the active Legacy Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param name: New Pose Name, New name for pose
    :type name: str
    :param pose: Pose, The pose to rename
    :type pose: typing.Union[str, int]
    '''

    pass


def restore_previous_action(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: bool = None):
    ''' Switch back to the previous Action, after creating a pose asset :file: addons/pose_library/operators.py\:163 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$163> _

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def unlink(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Deprecated, will be removed in Blender 3.3. Remove Legacy Pose Library from active Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass
