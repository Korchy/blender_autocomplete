import sys
import typing


def action_sanitize():
    ''' Make action suitable for use as a Pose Library

    '''

    pass


def apply_pose(pose_index: int = -1):
    ''' Apply specified Pose Library pose to the rig

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
    ''' Apply the given Pose Action to the rig :file: addons/pose_library/operators.py\:445 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$445> _

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
    ''' Blend the given Pose Action to the rig :file: addons/pose_library/operators.py\:419 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$419> _

    '''

    pass


def browse_interactive(pose_index: int = -1):
    ''' Interactively browse poses in 3D-View

    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: int
    '''

    pass


def convert_old_poselib():
    ''' Create a pose asset for each pose marker in the current action :file: addons/pose_library/operators.py\:467 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$467> _

    '''

    pass


def copy_as_asset():
    ''' Create a new pose asset on the clipboard, to be pasted into an Asset Browser :file: addons/pose_library/operators.py\:226 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$226> _

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
    ''' Add New Pose Library to active Object

    '''

    pass


def paste_asset():
    ''' Paste the Asset that was previously copied using Copy As Asset :file: addons/pose_library/operators.py\:301 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$301> _

    '''

    pass


def pose_add(frame: int = 1, name: str = "Pose"):
    ''' Add the current Pose to the active Pose Library

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


def pose_move(pose: typing.Union[int, str] = '',
              direction: typing.Union[int, str] = 'UP'):
    ''' Move the pose up or down in the active Pose Library

    :param pose: Pose, The pose to move
    :type pose: typing.Union[int, str]
    :param direction: Direction, Direction to move the chosen pose towards
    :type direction: typing.Union[int, str]
    '''

    pass


def pose_remove(pose: typing.Union[int, str] = ''):
    ''' Remove nth pose from the active Pose Library

    :param pose: Pose, The pose to remove
    :type pose: typing.Union[int, str]
    '''

    pass


def pose_rename(name: str = "RenamedPose", pose: typing.Union[int, str] = ''):
    ''' Rename specified pose from the active Pose Library

    :param name: New Pose Name, New name for pose
    :type name: str
    :param pose: Pose, The pose to rename
    :type pose: typing.Union[int, str]
    '''

    pass


def restore_previous_action():
    ''' Switch back to the previous Action, after creating a pose asset :file: addons/pose_library/operators.py\:179 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$179> _

    '''

    pass


def unlink():
    ''' Remove Pose Library from active Object

    '''

    pass
