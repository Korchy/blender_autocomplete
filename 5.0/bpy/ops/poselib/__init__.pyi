import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def apply_pose_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    asset_library_type: bpy.stub_internal.rna_enums.AssetLibraryTypeItems
    | None = "LOCAL",
    asset_library_identifier: str = "",
    relative_asset_identifier: str = "",
    blend_factor: float | None = 1.0,
    flipped: bool | None = False,
) -> None:
    """Apply the given Pose Action to the rig

    :param asset_library_type: Asset Library Type
    :param asset_library_identifier: Asset Library Identifier
    :param relative_asset_identifier: Relative Asset Identifier
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    """

def asset_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete the selected Pose Asset"""

def asset_modify(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["ADJUST", "REPLACE", "ADD", "REMOVE"] | None = "ADJUST",
) -> None:
    """Update the selected pose asset in the asset library from the currently selected bones. The mode defines how the asset is updated

        :param mode: Overwrite Mode, Specify which parts of the pose asset are overwritten

    ADJUST
    Adjust -- Update existing channels in the pose asset but dont remove or add any channels.

    REPLACE
    Replace with Selection -- Completely replace all channels in the pose asset with the current selection.

    ADD
    Add Selected Bones -- Add channels of the selection to the pose asset. Existing channels will be updated.

    REMOVE
    Remove Selected Bones -- Remove channels of the selection from the pose asset.
    """

def blend_pose_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    asset_library_type: bpy.stub_internal.rna_enums.AssetLibraryTypeItems
    | None = "LOCAL",
    asset_library_identifier: str = "",
    relative_asset_identifier: str = "",
    blend_factor: float | None = 0.0,
    flipped: bool | None = False,
    release_confirm: bool | None = False,
) -> None:
    """Blend the given Pose Action to the rig

    :param asset_library_type: Asset Library Type
    :param asset_library_identifier: Asset Library Identifier
    :param relative_asset_identifier: Relative Asset Identifier
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    """

def copy_as_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new pose asset on the clipboard, to be pasted into an Asset Browser"""

def create_pose_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pose_name: str = "",
    asset_library_reference: str | None = "",
    catalog_path: str = "",
) -> None:
    """Create a new asset from the selected bones in the scene

    :param pose_name: Pose Name, Name for the new pose asset
    :param asset_library_reference: Library, Asset library used to store the new pose
    :param catalog_path: Catalog, Catalog to use for the new asset
    """

def paste_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste the Asset that was previously copied using Copy As Asset"""

def pose_asset_select_bones(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
    flipped: bool | None = False,
) -> None:
    """Select those bones that are used in this pose

    :param select: Select
    :param flipped: Flipped
    """

def restore_previous_action(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Switch back to the previous Action, after creating a pose asset"""
