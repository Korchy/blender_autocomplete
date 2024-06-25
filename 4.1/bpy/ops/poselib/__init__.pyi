import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def apply_pose_asset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    blend_factor: typing.Any | None = 1.0,
    flipped: bool | typing.Any | None = False,
):
    """Apply the given Pose Action to the rig

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
    :type blend_factor: typing.Any | None
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: bool | typing.Any | None
    """

    ...

def blend_pose_asset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    blend_factor: typing.Any | None = 0.0,
    flipped: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Blend the given Pose Action to the rig

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
    :type blend_factor: typing.Any | None
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: bool | typing.Any | None
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: bool | typing.Any | None
    """

    ...

def convert_old_object_poselib(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a pose asset for each pose marker in this legacy pose library data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def convert_old_poselib(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a pose asset for each pose marker in the current action

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def copy_as_asset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a new pose asset on the clipboard, to be pasted into an Asset Browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def create_pose_asset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    pose_name: str | typing.Any = "",
    activate_new_action: bool | typing.Any | None = True,
):
    """Create a new Action that contains the pose of the selected bones, and mark it as Asset. The asset will be stored in the current blend file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param pose_name: Pose Name
    :type pose_name: str | typing.Any
    :param activate_new_action: Activate New Action
    :type activate_new_action: bool | typing.Any | None
    """

    ...

def paste_asset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Paste the Asset that was previously copied using Copy As Asset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def pose_asset_select_bones(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
    flipped: bool | typing.Any | None = False,
):
    """Select those bones that are used in this pose

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | typing.Any | None
    :param flipped: Flipped
    :type flipped: bool | typing.Any | None
    """

    ...

def restore_previous_action(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Switch back to the previous Action, after creating a pose asset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
