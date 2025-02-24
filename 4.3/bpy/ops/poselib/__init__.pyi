import typing
import collections.abc
import typing_extensions

def apply_pose_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    blend_factor: float | None = 1.0,
    flipped: bool | None = False,
):
    """Apply the given Pose Action to the rig

    :type execution_context: int | str | None
    :type undo: bool | None
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
    :type blend_factor: float | None
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: bool | None
    """

def blend_pose_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    blend_factor: float | None = 0.0,
    flipped: bool | None = False,
    release_confirm: bool | None = False,
):
    """Blend the given Pose Action to the rig

    :type execution_context: int | str | None
    :type undo: bool | None
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
    :type blend_factor: float | None
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: bool | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | None
    """

def convert_old_object_poselib(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create a pose asset for each pose marker in this legacy pose library data-block

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def convert_old_poselib(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Create a pose asset for each pose marker in the current action

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy_as_asset(execution_context: int | str | None = None, undo: bool | None = None):
    """Create a new pose asset on the clipboard, to be pasted into an Asset Browser

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def create_pose_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pose_name: str = "",
    activate_new_action: bool | None = True,
):
    """Create a new Action that contains the pose of the selected bones, and mark it as Asset. The asset will be stored in the current blend file

    :type execution_context: int | str | None
    :type undo: bool | None
    :param pose_name: Pose Name
    :type pose_name: str
    :param activate_new_action: Activate New Action
    :type activate_new_action: bool | None
    """

def paste_asset(execution_context: int | str | None = None, undo: bool | None = None):
    """Paste the Asset that was previously copied using Copy As Asset

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def pose_asset_select_bones(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
    flipped: bool | None = False,
):
    """Select those bones that are used in this pose

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    :param flipped: Flipped
    :type flipped: bool | None
    """

def restore_previous_action(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Switch back to the previous Action, after creating a pose asset

    :type execution_context: int | str | None
    :type undo: bool | None
    """
