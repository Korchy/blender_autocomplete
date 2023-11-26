import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def apply_pose_asset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        blend_factor: typing.Optional[typing.Any] = 1.0,
        flipped: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Apply the given Pose Action to the rig

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
    :type blend_factor: typing.Optional[typing.Any]
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def blend_pose_asset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        blend_factor: typing.Optional[typing.Any] = 0.0,
        flipped: typing.Optional[typing.Union[bool, typing.Any]] = False,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Blend the given Pose Action to the rig

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
    :type blend_factor: typing.Optional[typing.Any]
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: typing.Optional[typing.Union[bool, typing.Any]]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def convert_old_object_poselib(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create a pose asset for each pose marker in this legacy pose library data-block :File: `addons/pose_library/operators.py\:435 <https://projects.blender.org/blender/blender-addons/addons/pose_library/operators.py#L435>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def convert_old_poselib(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create a pose asset for each pose marker in the current action :File: `addons/pose_library/operators.py\:401 <https://projects.blender.org/blender/blender-addons/addons/pose_library/operators.py#L401>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def copy_as_asset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create a new pose asset on the clipboard, to be pasted into an Asset Browser :File: `addons/pose_library/operators.py\:211 <https://projects.blender.org/blender/blender-addons/addons/pose_library/operators.py#L211>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def create_pose_asset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        pose_name: typing.Union[str, typing.Any] = "",
        activate_new_action: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True):
    ''' Create a new Action that contains the pose of the selected bones, and mark it as Asset. The asset will be stored in the current blend file :File: `addons/pose_library/operators.py\:84 <https://projects.blender.org/blender/blender-addons/addons/pose_library/operators.py#L84>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param pose_name: Pose Name
    :type pose_name: typing.Union[str, typing.Any]
    :param activate_new_action: Activate New Action
    :type activate_new_action: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def paste_asset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Paste the Asset that was previously copied using Copy As Asset :File: `addons/pose_library/operators.py\:283 <https://projects.blender.org/blender/blender-addons/addons/pose_library/operators.py#L283>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def pose_asset_select_bones(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        select: typing.Optional[typing.Union[bool, typing.Any]] = True,
        flipped: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select those bones that are used in this pose :File: `addons/pose_library/operators.py\:321 <https://projects.blender.org/blender/blender-addons/addons/pose_library/operators.py#L321>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Optional[typing.Union[bool, typing.Any]]
    :param flipped: Flipped
    :type flipped: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def restore_previous_action(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Switch back to the previous Action, after creating a pose asset :File: `addons/pose_library/operators.py\:160 <https://projects.blender.org/blender/blender-addons/addons/pose_library/operators.py#L160>`__

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
