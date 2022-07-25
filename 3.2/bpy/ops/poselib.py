import sys
import typing


def action_sanitize():
    ''' Deprecated, will be removed in Blender 3.3. Make action suitable for use as a Legacy Pose Library

    '''

    pass


def apply_pose(pose_index: int = -1):
    ''' Deprecated, will be removed in Blender 3.3. Apply specified Legacy Pose Library pose to the rig

    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: int
    '''

    pass


def apply_pose_asset(blend_factor: float = 1.0, flipped: bool = False):
    ''' Apply the given Pose Action to the rig

    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses
    :type blend_factor: float
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: bool
    '''

    pass


def apply_pose_asset_for_keymap():
    ''' Apply the given Pose Action to the rig :file: addons/pose_library/operators.py\:431 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$431> _

    '''

    pass


def blend_pose_asset(blend_factor: float = 0.0,
                     flipped: bool = False,
                     release_confirm: bool = False):
    ''' Blend the given Pose Action to the rig

    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses
    :type blend_factor: float
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool
    '''

    pass


def blend_pose_asset_for_keymap():
    ''' Blend the given Pose Action to the rig :file: addons/pose_library/operators.py\:403 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$403> _

    '''

    pass


def browse_interactive(pose_index: int = -1):
    ''' Deprecated, will be removed in Blender 3.3. Interactively browse Legacy Pose Library poses in 3D-View

    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: int
    '''

    pass


def convert_old_object_poselib():
    ''' Create a pose asset for each pose marker in this legacy pose library data-block :file: addons/pose_library/operators.py\:487 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$487> _

    '''

    pass


def convert_old_poselib():
    ''' Create a pose asset for each pose marker in the current action :file: addons/pose_library/operators.py\:453 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$453> _

    '''

    pass


def copy_as_asset():
    ''' Create a new pose asset on the clipboard, to be pasted into an Asset Browser :file: addons/pose_library/operators.py\:210 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$210> _

    '''

    pass


def create_pose_asset(pose_name: str = "", activate_new_action: bool = True):
    ''' Create a new Action that contains the pose of the selected bones, and mark it as Asset. The asset will be stored in the current blend file

    :param pose_name: Pose Name
    :type pose_name: str
    :param activate_new_action: Activate New Action
    :type activate_new_action: bool
    '''

    pass


def new():
    ''' Deprecated, will be removed in Blender 3.3. Add New Legacy Pose Library to active Object

    '''

    pass


def paste_asset():
    ''' Paste the Asset that was previously copied using Copy As Asset :file: addons/pose_library/operators.py\:285 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$285> _

    '''

    pass


def pose_add(frame: int = 1, name: str = "Pose"):
    ''' Deprecated, will be removed in Blender 3.3. Add the current Pose to the active Legacy Pose Library

    :param frame: Frame, Frame to store pose on
    :type frame: int
    :param name: Pose Name, Name of newly added Pose
    :type name: str
    '''

    pass


def pose_asset_select_bones(select: bool = True, flipped: bool = False):
    ''' Select those bones that are used in this pose

    :param select: Select
    :type select: bool
    :param flipped: Flipped
    :type flipped: bool
    '''

    pass


def pose_move(pose: typing.Union[str, int] = '',
              direction: typing.Union[str, int] = 'UP'):
    ''' Deprecated, will be removed in Blender 3.3. Move the pose up or down in the active Legacy Pose Library

    :param pose: Pose, The pose to move
    :type pose: typing.Union[str, int]
    :param direction: Direction, Direction to move the chosen pose towards
    :type direction: typing.Union[str, int]
    '''

    pass


def pose_remove(pose: typing.Union[str, int] = ''):
    ''' Deprecated, will be removed in Blender 3.3. Remove nth pose from the active Legacy Pose Library

    :param pose: Pose, The pose to remove
    :type pose: typing.Union[str, int]
    '''

    pass


def pose_rename(name: str = "RenamedPose", pose: typing.Union[str, int] = ''):
    ''' Deprecated, will be removed in Blender 3.3. Rename specified pose from the active Legacy Pose Library

    :param name: New Pose Name, New name for pose
    :type name: str
    :param pose: Pose, The pose to rename
    :type pose: typing.Union[str, int]
    '''

    pass


def restore_previous_action():
    ''' Switch back to the previous Action, after creating a pose asset :file: addons/pose_library/operators.py\:163 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$163> _

    '''

    pass


def unlink():
    ''' Deprecated, will be removed in Blender 3.3. Remove Legacy Pose Library from active Object

    '''

    pass
