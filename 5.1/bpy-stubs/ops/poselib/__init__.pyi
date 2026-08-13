import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops
import bpy.stub_internal.rna_enums

class apply_pose_asset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        asset_library_type: typing.Literal[
            bpy.stub_internal.rna_enums.AssetLibraryTypeItems
        ]
        | None = "LOCAL",
        asset_library_identifier: str = "",
        relative_asset_identifier: str = "",
        blend_factor: float | None = 1.0,
        flipped: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Apply the given Pose Action to the rig

        :param execution_context:
        :param undo:
        :param asset_library_type: Asset Library Type, (optional)
        :param asset_library_identifier: Asset Library Identifier, (optional, never None)
        :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
        :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it (in [-inf, inf], optional)
        :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis (optional)
        :return: Result of the operator call.
        """

class asset_delete(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Delete the selected Pose Asset

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class asset_modify(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        mode: typing.Literal["ADJUST", "REPLACE", "ADD", "REMOVE"] | None = "ADJUST",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Update the selected pose asset in the asset library from the currently selected bones. The mode defines how the asset is updated

                :param execution_context:
                :param undo:
                :param mode: Overwrite Mode, Specify which parts of the pose asset are overwritten (optional)

        ADJUST
        Adjust -- Update existing channels in the pose asset but dont remove or add any channels.

        REPLACE
        Replace with Selection -- Completely replace all channels in the pose asset with the current selection.

        ADD
        Add Selected Bones -- Add channels of the selection to the pose asset. Existing channels will be updated.

        REMOVE
        Remove Selected Bones -- Remove channels of the selection from the pose asset.
                :return: Result of the operator call.
        """

class blend_pose_asset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        asset_library_type: typing.Literal[
            bpy.stub_internal.rna_enums.AssetLibraryTypeItems
        ]
        | None = "LOCAL",
        asset_library_identifier: str = "",
        relative_asset_identifier: str = "",
        blend_factor: float | None = 0.0,
        flipped: bool | None = False,
        release_confirm: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Blend the given Pose Action to the rig

        :param execution_context:
        :param undo:
        :param asset_library_type: Asset Library Type, (optional)
        :param asset_library_identifier: Asset Library Identifier, (optional, never None)
        :param relative_asset_identifier: Relative Asset Identifier, (optional, never None)
        :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it (in [-inf, inf], optional)
        :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis (optional)
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button (optional)
        :return: Result of the operator call.
        """

class copy_as_asset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new pose asset on the clipboard, to be pasted into an Asset Browser

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class create_pose_asset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        pose_name: str = "",
        asset_library_reference: str | None = "",
        catalog_path: str = "",
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Create a new asset from the selected bones in the scene

        :param execution_context:
        :param undo:
        :param pose_name: Pose Name, Name for the new pose asset (optional, never None)
        :param asset_library_reference: Library, Asset library used to store the new pose (optional)
        :param catalog_path: Catalog, Catalog to use for the new asset (optional, never None)
        :return: Result of the operator call.
        """

class paste_asset(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Paste the Asset that was previously copied using Copy As Asset

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """

class pose_asset_select_bones(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
        *,
        select: bool | None = True,
        flipped: bool | None = False,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Select those bones that are used in this pose

        :param execution_context:
        :param undo:
        :param select: Select, (optional)
        :param flipped: Flipped, (optional)
        :return: Result of the operator call.
        """

class restore_previous_action(bpy.ops._BPyOpsSubModOp):
    def __new__(
        cls,
        execution_context: int | str | None = None,
        undo: bool | None = None,
        /,
    ) -> set[typing.Literal[bpy.stub_internal.rna_enums.OperatorReturnItems]]:
        """Switch back to the previous Action, after creating a pose asset

        :param execution_context:
        :param undo:
        :return: Result of the operator call.
        """
